# Site Residual Image Final Audit — 2026-09-19

## Scope

Normal HTML pages on `develop`, using the current residual-image inventory after completion of FEM / Heat / Appendix / Hydronamics / Physics / Mesh / Column / Counting formula work.

## Final residual inventory

- Normal HTML pages scanned: **205**
- Residual Word-export image placements: **161**
- Missing referenced assets: **49**
- Residual placements with existing source images: **112**
- Unclassified existing residual placements: **0**

| Section | Residual placements | Final classification |
|---|---:|---|
| `mps` | 49 | **HOLD: source GIF missing** |
| `fem` | 33 | verified retained diagram / mixed illustration |
| `mesh` | 23 | verified retained diagram / graph / result image |
| `hydronamics` | 21 | verified retained diagram / mixed illustration |
| `physics` | 16 | verified retained diagram / mixed illustration |
| `appendix` | 9 | verified retained diagram / mixed illustration |
| `heat` | 8 | verified retained diagram / mixed illustration |
| `counting` | 2 | verified flowchart |
| **Total** | **161** | **112 verified retained + 49 MPS HOLD** |

## MPS source recovery status

The 49 MPS references remain unresolved as source assets.

- `develop`: source files absent
- `release_1.0.0`: source files absent
- oldest reachable Git tree: source files absent
- HTML / BAK files: references only; no embedded source images
- production FTPS read-only recovery run **35408141850**: **0/49 recovered**
- production `/img`: no MPS-related directories were found
- prior project notes confirm that `HP.7z` contained legacy Word manuscripts, but the archive itself and exact MPS Word filenames are not available in the current runtime

Under the strict source policy, standard MPS formulas from external literature are **not** accepted as a substitute for the original source images.

## Conclusion

- **Known formula conversion outside MPS: complete**
- **Existing residual images outside MPS: all classified and intentionally retained**
- **Unknown existing formula images outside MPS: 0**
- **MPS missing references: 49, HOLD pending original-source recovery**
- Production FTP deployment has not been performed.

## Supporting records

- `.document/formula_reviews/SITE_INLINE_IMAGE_INVENTORY_20260918.md`
- `.document/formula_reviews/MPS_REMOTE_SOURCE_RECOVERY_20260919.md`
- `.document/formula_reviews/STRICT_SOURCE_AUDIT_STATUS.md`
- category-specific retained-image final audit records under `.document/formula_reviews/`
