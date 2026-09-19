# MPS Remote Source Recovery — 2026-09-19

## Current status

Production FTPS connectivity was rechecked in read-only mode after MPS formula conversion completed.

- latest run: `35408141850`
- latest job: `105836951290`
- checkout: latest `develop`
- FTPS connect/login: **success**
- TLS data protection (`PROT P`): **success**
- passive mode: **success**
- remote `/img` read access: **reached**
- remote write/delete: **none**
- current MPS `<img ...files/imageNNN.gif>` references: **0**
- current MPS missing formula images: **0**

## Why the latest job concluded failure

The legacy recovery workflow still contained an old assertion:

```text
Expected 49 MPS references but parsed 0
```

This assertion ran **after** FTPS connection/login and remote read access succeeded.

The current site correctly has zero MPS formula-image references because all 49 MPS formula positions are now MathJax:
- source-exact / recovered: **48**
- user-approved inferred reconstruction: **1**
- total: **49**

The workflow expectation has since been updated from 49 to 0.

## Historical recovery result

Before MathJax replacement, production FTPS did not contain the 49 referenced MPS GIF assets.
That historical result led to the Word/Visio/archive recovery work.

The historical missing-49 state is no longer the current HTML state.

## Current deployment interpretation

- FTPS credentials/connectivity: **verified**
- production remote mutation in this check: **none**
- MPS missing images: **0**
- MPS HOLD: **0**
- production deployment: **not performed**
