# Brand Context — AIMax issue 006

Original skill by Arnab Bag / arnabbagxd. MIT notice preserved.

## Install
Extract the complete brand-context folder into your assistant's supported skills directory. Open SKILL.md before using it. Ask: "Set brand context for this project." Provide only information you are authorized to store. The source writes .agents/brand-context.md or reads .claude/brand-context.md; actual host behavior may differ. Review an existing file before any update. Saving a file does not itself prove automatic loading.

## Run the isolated demonstration
Python 3.9+ standard library, no network or install dependencies:

```sh
python3 demo/run_demo.py
```

The fictional RelayDesk brief has six sections and eighteen fields. The demo changes only tone, preserves seventeen other fields, and rejects three missing-field examples plus a stale-hash update. It writes only demo/output. Its two copy examples are AIMax-authored, not independent model outputs. The completeness validator cannot verify truth or quality.

Read CURATION.md, TRACE-REVIEW.md and demo/results.json for provenance and limits.
