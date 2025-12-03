# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-03

### Added
- Project configuration files for modern Python tooling
  - `requirements.txt` - Package dependencies with version constraints
  - `pyproject.toml` - Project metadata and tool configurations (Black, isort, Pylint)
  - `.editorconfig` - Editor consistency settings
  - `CONTRIBUTING.md` - Contribution guidelines and code standards
  - `CHANGELOG.md` - Project history documentation
- Automated test suite (`tests/test_syntax_and_imports.py`)
  - Syntax validation for all Python files
  - Python 3 compatibility checks
  - String formatting validation
- README files for each directory explaining contents and purpose

### Changed
- **BREAKING**: Renamed all 56 Python files from spaces to snake_case convention
  - Example: `PHYS613 A10 Exercise6.10 FFT.py` → `phys613_a10_exercise6_10_fft.py`
  - Improves CLI compatibility and follows PEP 8 guidelines
  - **Impact**: Any scripts or imports referencing old filenames must be updated
- Reorganized project structure by course and topic
  - Created `phys510/` for PHYS 510 course materials
  - Created `phys613/assignments/` for weekly assignments
  - Created `phys613/projects/` for major projects
  - Created `clusters/` for cluster simulations
  - Created `examples/` for demonstration programs
  - Created `tests/` for test suite
- Migrated entire codebase from Python 2 to Python 3
  - All `print` statements → `print()` functions
  - String formatting modernized to f-strings
  - Math operations use NumPy functions (`np.sqrt()`, `np.exp()`, etc.)
  - Pythonic idioms throughout (negative indexing, augmented operators, `zip()`)
- Updated main README with comprehensive documentation
  - Installation instructions
  - Project structure overview
  - Testing guidelines
  - Configuration file descriptions

### Fixed
- All escape sequence warnings in matplotlib LaTeX strings
  - Converted to raw strings: `r'$\omega$'` instead of `'$\omega$'`
  - Affects labels, titles, and annotations in ~15 files
- Python 2 print statements in 9 files that were missed in initial pass
- Octal literal syntax error in `phys613_project1_p2_minimize.py`

## [0.2.0] - 2025-12-02

### Changed
- Initial Python 3 modernization pass
- Updated 40+ files with Python 3 syntax
- Consolidated imports to use NumPy

## [0.1.0] - Earlier

### Added
- Initial computational physics simulations and coursework
- Topics: quantum mechanics, ODEs, PDEs, Monte Carlo, FFT, optimization
- Course materials from PHYS 510 and PHYS 613

---

## Migration Guide

### For Users Updating from Pre-1.0.0

**File Renames**: If you have scripts that import or reference files from this repository, you'll need to update the filenames:

```python
# Old (pre-1.0.0)
from "PHYS613 A10 Exercise6.10 FFT" import something

# New (1.0.0+)
from phys613.assignments.phys613_a10_exercise6_10_fft import something
```

**Directory Structure**: Files have moved into organized directories:
- Root files → topic-specific directories (`phys510/`, `phys613/`, `clusters/`, `examples/`)
- All course materials now under `phys613/assignments/` or `phys613/projects/`

### Compatibility Notes

- **Python Version**: Minimum Python 3.7, tested on 3.9+
- **NumPy Version**: Minimum 1.21.0 (uses modern array APIs)
- **Matplotlib**: Minimum 3.4.0
- **SciPy**: Minimum 1.7.0

---

[1.0.0]: https://github.com/elkins/ComputationalPhysics/compare/v0.2.0...v1.0.0
[0.2.0]: https://github.com/elkins/ComputationalPhysics/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/elkins/ComputationalPhysics/releases/tag/v0.1.0
