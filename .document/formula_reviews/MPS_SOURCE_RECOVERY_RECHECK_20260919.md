# MPS Source Recovery Recheck — 2026-09-19

> **Superseded by:** `.document/formula_reviews/MPS_SOURCE_RECOVERY_AND_FORMULA_AUDIT_20260919.md`

The earlier recheck concluded that the Library 7z existed but could not be materialized directly.
A later recovery path succeeded:

**Library → Google Drive copy → raw-file download → libarchive extraction**

Current status:

- `HP(1).7z` recovered and extracted successfully.
- MPS Word and Visio source files were recovered.
- Original site GIF binaries are still absent from the archive.
- **48/49** formula references have recoverable Word Equation.3 source and have been reflected as MathJax on `develop`.
- `mps/mps_6_2.html -> image022.gif` has no authoritative recoverable Word/Visio source and remains **SOURCE BLOCKED / HOLD**.
- Targeted MPS Browser QA is recorded separately in `MPS_FINAL_BROWSER_QA_20260919.md`.

Do not use the earlier “HP.7z cannot be extracted” conclusion as the current state.
