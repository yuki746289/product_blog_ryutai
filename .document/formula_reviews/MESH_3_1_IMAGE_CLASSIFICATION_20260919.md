# Mesh 3_1 Image Classification — 2026-09-19

Created: 2026-09-19T07:12:00+09:00

## Scope

- Page: `mesh/mesh_3_1.html`
- Source directory: `img/mesh_node_buble.files`
- Placements: **19**
- Canonical source: original HP images

| Classification | Count |
|---|---:|
| Display formula | **5** |
| Inline formula | **4** |
| Retained diagram / graph / result image | **10** |
| Total | **19** |

## Formula targets

Inline:
- `image004.png`: position vector p1
- `image005.png`: position vector p2
- `image012.png`: node deletion condition `n(r_i)>8`
- `image013.png`: node addition condition `n(r_i)<5`

Display:
- `image006.png`: two-node force expression
- `image009.png`: summed force from surrounding nodes
- `image010.png`: timestep direction-vector expression
- `image014.png`: weighted-average radius correction
- `image015.png`: weight function

## Retained images

- `image001.png`: x/y/z coordinate-axis diagram
- `image002.png`: attraction geometry
- `image003.png`: repulsion geometry
- `image007.png`: weight-function graph showing attraction/repulsion regions
- `image008.png`: surrounding-node geometry
- `image011.png`: local node-density geometry
- `image016.jpg`–`image019.jpg`: numerical-result screenshots

## Mixed text/formula handling

`image012.png` and `image013.png` contain Japanese labels plus formulas. The normal HTML already contains the same labels (`節点削除：`, `節点追加：`) immediately before the image, so the image replacement converts only the formula component to inline MathJax. The explanatory Japanese text remains HTML text.

## Source-visible notation that must not be normalized

`image006.png` visibly uses
`|\\vec{p}_2-\\vec{p}_2|`
in the denominator of the direction factor. This is retained exactly even though it is mathematically problematic.

Production deployment has not been performed.
