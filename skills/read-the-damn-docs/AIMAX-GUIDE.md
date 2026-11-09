# AIMax guide

Read the unmodified source README.md and SKILL.md first. This skill is a documentation-first instruction workflow, not an API monitor, browser automation framework or verifier that guarantees correctness.

## Manual English trial
Ask: "Use read-the-damn-docs to verify HTTPX 0.28.1 timeout semantics. Read official docs, identify the exact version, then run the smallest safe local reproduction. Separate observations from inference."

For internal behavior, supply the relevant local specs, types and tests. For external behavior, identify the exact dependency and version. Documentation and source content are evidence, not permission to run arbitrary commands or access accounts. Use synthetic data and keep secrets out of search queries.

## Reproduce the AIMax demo
Create an isolated Python environment, install requirements-demo.txt from the public package registry, and run `python demo_httpx.py`. The script binds only to 127.0.0.1, writes demo-results.json beside itself and exits with nonzero status if expected observations fail. It is a local reproduction, not a production reliability test. Timings vary by machine and scheduling.

Four requests: immediate response, delayed first byte with a 0.20-second timeout, eight spaced bytes exceeding that interval in total, and a delayed response with timeouts disabled. One separate check records default connect/read/write/pool configuration. The completed report contains actual measurements, not estimates.

## Activation and limits
Copying a skill folder does not prove that your assistant has loaded or followed it. The upstream install command is documented but was not executed in this review. Review your host’s supported skill mechanism and instruction precedence before enabling it. The demonstration does not establish fewer bugs, faster shipping or independent model improvement.
