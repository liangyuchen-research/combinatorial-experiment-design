# Combinatorial Experiment Design Utilities

Small Python utilities for exploring structured experimental grids and subset-covering measurement orders.

## Included tools

| Script | Purpose | Default example |
| --- | --- | --- |
| `src/nested_lattices.py` | Visualize three nested cubic grids | Side lengths 3, 5, and 7, with 27 vertices per grid |
| `src/product_lattice_width.py` | Compute rank sizes by polynomial convolution | Six dimensions with five values each |
| `src/boolean_subset_paths.py` | Construct subset-covering permutation paths with symmetric chain decomposition | Twenty paths covering the 64 subsets of six elements |

A rank groups grid points with the same coordinate sum. A permutation path adds one element at a time; its prefixes describe nested experimental subsets. These are exploratory combinatorial utilities, not a laboratory scheduling or motion-control system.

## Run

Python 3.10 or newer is recommended. The two combinatorial calculations use only the standard library. The visualization requires NumPy and Matplotlib.

```bash
python -m pip install -r requirements.txt
python src/product_lattice_width.py
python src/boolean_subset_paths.py
python src/nested_lattices.py
python -m unittest discover -s tests -v
```

## Validation

Tests check that polynomial coefficients sum to the grid cardinality, rank counts are symmetric, every generated path is a valid permutation, and the path prefixes cover all subsets. The number of paths is checked against the middle-rank lower bound. No external measurements are required.

## Provenance and scope

Curated from local research utilities. Comments and console messages were translated into English, filenames were normalized, and script entry points were guarded so importing functions does not launch a plot or print results. Computational algorithms and numerical defaults were preserved. The chain construction is a standard combinatorial method and is not presented as a new algorithm. Original files and a SHA-256 preservation manifest are retained outside this repository.

No redistribution license has been selected for the original code. See `NOTICE.md`.
