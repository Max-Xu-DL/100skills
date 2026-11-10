# Brand Positioning — AIMax curated edition

A seven-part English workflow for a founder, consultant or agency defining a brand's category, audience, alternatives, positioning statement, supporting proof and boundaries.

## Install

Unzip and place the `brand-positioning` folder in your host's skill directory (for Codex, `~/.codex/skills/brand-positioning`). Keep SKILL.md and LICENSE together. Host support and activation behavior vary; this package does not install or execute itself.

## Start

Tell your assistant: “Use brand-positioning to position our client approval workspace for small creative agencies. Separate supplied facts from hypotheses and ask for missing inputs.” Provide an approved, redacted brand brief. If your workspace uses `.agents/brand-context.md`, review that file before sharing it. Do not include private client details or credentials.

Read the original SKILL.md for the seven outputs. `demo/brief.json` and `demo/positioning.json` are a fictional English worked example authored by AIMax. Run `python3 demo/validate_demo.py` to reproduce its eight deterministic checks and four negative-case rejections. Standard library only; no network calls. Running this validator checks the authored report, not a model's execution of the skill.

## Evidence

TRACE-REVIEW.md: 20-item semantic review, 3.65/5. Separate original companion structural base: 3.77/5. Original strict all-5 gate not passed. The original rubric rewards Chinese localization; this source remains English. No certification or runtime benchmark is claimed. `evals/evals.json` contains two preserved, unexecuted upstream author fixtures.

See CURATION.md and LICENSE for source, attribution and the unchanged upstream snapshot. Feature facts can support a positioning promise; competitive defensibility requires evidence beyond this fictional brief.
