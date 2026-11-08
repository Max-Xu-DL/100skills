# AIMax usage guide

Read the original README.md and SKILL.md first. This is an English response convention, not a task runner or an independent verifier.

## Try manually
Ask: "Use quick-recap for this work unit. End with one status line supported by the evidence." Provide the real requested outcome and what is complete or missing. Review the entire response, including the final line.

## Persistent activation
The upstream README recommends a managed AGENTS.md / CLAUDE.md block and an installer command using --update-instructions. AIMax did not execute or audit the installer implementation. A copied skill folder alone does not establish automatic activation. Review the target instruction file and host support before making persistent changes. This ZIP does not install a global behavior.

## Evidence and privacy
Green describes completed work; yellow names a specific non-routine follow-up; red is reserved for a missing user input that prevents continuation. Green must match the requested scope: a saved draft is not a published post. Do not paste secret values into status lines. Ask the user to configure credentials through the intended secure channel.

## Demonstration
Run `python3 scripts/validate_demo.py` from this directory. It checks six synthetic English fixture outputs and rejects four deliberately invalid examples. It does not run an agent, validate a real deployment or prove compliance in a future session. See evidence/demo-results.json and checker-review.md.
