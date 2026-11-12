# TRACE source review

Pinned skill-trace-checker 2.0.0 at 8e96b838746546aed3c77061e3e5ae7c15a83871. All twenty criteria applied by AI to the unmodified English source. AIMax additions are excluded. Equal-weight mean: **3.05/5** (display 3.05/5). Separate original structural evaluator base: **3.75/5**. Original strict all-5 gate: **not passed**. Not certification or target-skill execution. The original China-localization criterion penalizes this English source; it is retained without adding Chinese for points.

| ID | Criterion | Score | Source evidence | Improvement |
|---|---|---:|---|---|
| T1 | China localization | 2 | English-only instructions and triggers; no Chinese examples. | Add a separate localized edition only if needed; retain English source. |
| T2 | Safety | 3.5 | No executable source scripts or credential requests; no explicit prohibited-data list. | Add a safety section for internal brand inputs. |
| T3 | Boundary transparency | 3 | Before You Start and Related Skills bound capture/update work; no three-category boundary section. | Document supported, input-dependent and excluded tasks. |
| T4 | Data privacy | 1.5 | Audience language, competitors and business goals may be private; no redaction or storage guidance. | Explain local file privacy, redaction and permission requirements. |
| R1 | Exception handling | 3 | Ask for named missing fields and reuse supplied conversation facts; no precise error format. | Give field-specific missing-input responses. |
| R2 | Functional completeness | 4 | Six collection sections and matching output template cover the narrow brief task. | Add validation and multi-brand guidance. |
| R3 | Stability | 3 | Read existing file and ask what to update; no concurrent-edit or conflict strategy. | Read current content before scoped edits and detect stale updates. |
| R4 | Fallbacks | 3 | Alternative .claude path and related skills are listed; missing write permission and conflicting files are not handled. | Give a safe alternate output and file precedence rule. |
| A1 | Capability boundaries | 3 | Capture and update are explicit but no three categories with examples. | Add supported and out-of-scope examples. |
| A2 | Trigger precision | 4.5 | Description has six English trigger phrases and first-use detection; existing file routes to update. | Explain precedence when both context locations exist. |
| A3 | Audience breadth | 3.5 | General brand project foundation is broadly usable, but team governance is absent. | Show agency and multi-brand team workflows. |
| A4 | Customization | 4 | Personality, tone, audience language and values are explicit user-provided parameters. | Add conflict handling and optional fields. |
| C1 | Progressive disclosure | 2 | One short SKILL.md; no quick-start/deep-reference layers. | Add linked quick start and deeper guidance. |
| C2 | Structure | 4.5 | Clear six-section collection and copyable Markdown output; straightforward names. | Add navigation if expanded. |
| C3 | Anti-patterns | 1 | No common misuse examples or before/after corrections. | Add at least three misuse comparisons. |
| C4 | FAQ depth | 1 | No FAQ or deep FAQ files. | Add general and edge-case FAQs. |
| E1 | Output accuracy | 3 | Reuse supplied facts and structured fields reduce omissions; no explicit anti-invention rule and automatic-use claim overgeneralizes host behavior. | Mark unknowns, distinguish assumptions and qualify host loading. |
| E2 | Content completeness | 3.5 | Good minimal brief template; no evidence provenance, review date or edge-case reference. | Document source status and refresh rules. |
| E3 | Added value | 4 | Reusable file, update path and cross-skill context reuse go beyond a one-off questionnaire. | Add concrete multi-channel reuse examples. |
| E4 | Ready to use | 4 | Exact file path, output template and multiple trigger phrases are copyable; no finished example. | Add a complete fictional starter brief. |
