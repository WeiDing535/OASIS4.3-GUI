# Release checks for OASIS4.3-GUI-0.1

Checked on 2026-10-17 on Intel macOS with Python 3.12.

| Check | Result |
|---|---|
| Offline unit and regression suite | 157 passed; 1 real-reference test deselected |
| Pinned real 1TQW reference integration | 1 passed; 328,518 reflections; prepared SHA-256 matched |
| GUI construction without a display server | Passed; product title, sequence, copies, solvent and help controls present |
| Conda environment update and GUI launch | Passed |
| One-command installer in a fresh prefix | Passed |
| Wheel and source distribution metadata (`twine check`) | Passed |
| `CITATION.cff` schema 1.2.0 validation | Passed |
| Public-tree audit | Passed; no MTZ/PDB/mmCIF/NPZ target data or personal absolute paths |

The GitHub Actions workflow covers Linux, Windows, Intel macOS and Apple Silicon macOS. Those remote jobs have not run before the repository's first GitHub push, so their configured presence is not presented as a cross-platform pass.

The private 100-case benchmark is intentionally absent from this public repository. Historical aggregate benchmark observations are development evidence, not a blind external validation claim for this release.
