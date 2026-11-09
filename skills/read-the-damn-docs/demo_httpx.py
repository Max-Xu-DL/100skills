"""AIMax docs-first reproduction. Four loopback HTTP requests; no credentials.

Requires httpx==0.28.1. Does not install the source skill or benchmark an agent.
"""
import http.server
import threading
import time
import json
import platform
from pathlib import Path
import httpx

class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_GET(self):
        if self.path == '/delayed':
            time.sleep(0.50)
            body = b'delayed'
        elif self.path == '/stream':
            self.send_response(200)
            self.send_header('Content-Length', '8')
            self.end_headers()
            for _ in range(8):
                time.sleep(0.08)
                try:
                    self.wfile.write(b'x')
                    self.wfile.flush()
                except (BrokenPipeError, ConnectionResetError):
                    break
            return
        else:
            body = b'ok'
        try:
            self.send_response(200)
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError):
            pass

def main():
    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f'http://127.0.0.1:{server.server_port}'
    results = []
    with httpx.Client(trust_env=False) as client:
        t = client.timeout
        fields = {k: getattr(t, k) for k in ['connect', 'read', 'write', 'pool']}
        config = {'id': 'default-config', 'timeout_seconds': fields,
                  'passed': all(x == 5.0 for x in fields.values())}
        for name, route, timeout, expected in [
            ('immediate', '/ok', .20, 'success'),
            ('delayed-first-byte', '/delayed', .20, 'ReadTimeout'),
            ('stream-beyond-interval', '/stream', .20, 'success'),
            ('timeouts-disabled', '/delayed', None, 'success'),
        ]:
            started = time.perf_counter()
            body = None
            try:
                response = client.get(base + route, timeout=timeout)
                response.raise_for_status()
                body = response.text
                outcome = 'success'
            except httpx.TimeoutException as exc:
                outcome = type(exc).__name__
            elapsed = time.perf_counter() - started
            passed = outcome == expected
            if name == 'stream-beyond-interval':
                passed = passed and body == 'xxxxxxxx' and elapsed > .20
            results.append({'id': name, 'timeout_seconds': timeout,
                            'expected': expected, 'observed': outcome,
                            'body': body, 'elapsed_seconds': round(elapsed, 4),
                            'passed': passed})
    server.shutdown()
    server.server_close()
    report = {'method': 'AIMax-controlled loopback reproduction after reading official HTTPX docs',
              'httpx_version': httpx.__version__, 'python': platform.python_version(),
              'platform': platform.system(), 'external_requests_during_demo': 0,
              'configuration_check': config, 'requests': results,
              'passed': config['passed'] and all(x['passed'] for x in results),
              'limits': ['single local run per request scenario', 'not a production reliability benchmark',
                         'does not test automatic skill activation or independent model behavior']}
    dest = Path(__file__).parent / 'demo-results.json'
    dest.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    return 0 if report['passed'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
