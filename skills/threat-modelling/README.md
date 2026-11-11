# Threat Modelling — AIMax curated edition

An English STRIDE/SDL design-review workflow for SaaS teams and consultants. Define scope, draw data flows and trust boundaries, consider all six STRIDE categories, rank threats, then assign specific controls, owners, dates and verification work.

## Install and start

Extract the complete `threat-modelling` folder into your assistant host's skills directory (for Codex, `~/.codex/skills/threat-modelling`). Keep SKILL.md and LICENSE. Host activation behavior has not been tested here.

Try: “Use threat-modelling to review a multitenant client-file portal. State assumptions, show the DFD and boundaries, record every STRIDE category considered, and keep proposed controls separate from verified controls.” Supply an approved, redacted architecture brief; omit credentials and private customer data.

## Reproduce the local example

Run `python3 demo/run_demo.py`. Standard library only; no network or external packages. It demonstrates an intentionally weak in-memory file lookup and a tenant-scoped replacement, plus checks the authored report completeness. The English system and threat model are in demo/system.json and demo/threat-model.json. Six checks pass and three malformed report cases are rejected. This tests the tiny demonstration and document structure; it does not establish production security or model adherence.

## Review and provenance

TRACE-REVIEW.md records all 20 original rubric judgments, mean 3.78/5. Separate original companion structural base: 4.01/5. Original strict all-5 gate not passed. The rubric favors Chinese localization; this source remains English. No certification is claimed.

See CURATION.md and the unchanged LICENSE. Source metadata declares Microsoft and the copyright notice is preserved; the repository distributing this snapshot is vinayaklatthe/microsoft-security-skills. AIMax does not imply official endorsement. Threat modelling complements implementation review, scanning and testing.
