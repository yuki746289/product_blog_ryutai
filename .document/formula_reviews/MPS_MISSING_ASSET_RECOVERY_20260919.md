# MPS Missing Asset Recovery Audit — 2026-09-19

## Scope

MPS pages contain **49 inline GIF references** whose referenced files are absent from the repository.

| Page | Missing refs |
|---|---:|
| `mps/mps_1.html` | 1 |
| `mps/mps_2.html` | 1 |
| `mps/mps_3.html` | 12 |
| `mps/mps_4.html` | 9 |
| `mps/mps_5.html` | 2 |
| `mps/mps_6_1.html` | 2 |
| `mps/mps_6_2.html` | 22 |
| **Total** | **49** |

## Recovery checks

### 1. HTML / BAK consistency

For all seven MPS pages, the current `.html` and corresponding `.BAK` files reference the same image paths.
Therefore the missing references are not a recent HTML-path rewrite issue.

### 2. Git repository branches

Checked recursive trees for:
- `develop`
- `release_1.0.0`

Result:
- `img/mps*.files` assets present: **0**
- No recoverable MPS GIFs found in either preserved branch.

### 3. Production FTPS exact-file recovery

Workflow:
- `Recover missing MPS assets from FTPS`
- run **35408373561**

Attempted read-only RETR for all 49 exact paths.

Result:
- recovered: **0**
- missing: **49**
- server response: file not found for all targets.

No production write/delete operation was performed.

### 4. Production FTPS directory inventory

Workflow:
- `Inspect production MPS directories`
- final run **35408685270**

The server listing required CP932 decoding.
After correcting the listing encoding, the production `img` directory was enumerated successfully.

Result:
- no directory or file name containing `mps` exists under production `img`
- all seven expected `img/mps_*.files` directories are absent.

### 5. Public HTTP exact URLs

Workflow:
- `Recover missing MPS assets over HTTP`
- run **35408843344**

Checked all 49 public URLs under:
- `https://ryutai.ninja-web.net/img/.../imageNNN.gif`
- uppercase `.GIF` variant

Result:
- recovered: **0**
- HTTP 404 attempts: **98 / 98**

### 6. Internet Archive / Wayback

Workflow:
- `Recover MPS assets from Wayback`
- run **35408902368**

Queried CDX prefix indexes for all seven expected MPS asset directories.

Result:
- indexed rows: **0**
- recovered: **0 / 49**
- the 49 target GIF URLs are not present in the queried Wayback index.

### 7. Original HP archive / Word source

The personal Library still contains:
- `HP.7z`
- `HP(1).7z`
- `_tmp_HP_mps_recovery.7z`

The archive is known from prior work to contain old Word `.doc` source material.
However, in the current Project execution context the Library files cannot be materialized as raw bytes, and compressed-file contents are not readable through Files text extraction.

A Library filename scan found no separately extracted MPS Word manuscripts.

## Decision

**MPS 49 references remain BLOCKED because the canonical source bytes are unavailable in the current execution context.**

Do not:
- infer formulas from theory,
- reconstruct formulas from surrounding prose alone,
- replace the missing GIFs with guessed MathJax,
- claim source verification.

The existing rule remains authoritative: **no source → no formula conversion**.

## What is confirmed

- GitHub source: not present
- preserved branch: not present
- production FTPS: not present
- production HTTP: 404
- Wayback queried prefixes: not indexed
- HTML/BAK references: consistent
- HP archive: exists in Library, but raw archive bytes are inaccessible to this execution context

## Production status

No FTP deployment was performed as part of this recovery investigation.
