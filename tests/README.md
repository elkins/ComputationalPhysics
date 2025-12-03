# Tests

Automated test suite for the computational physics codebase.

## Running Tests

From the repository root:
```bash
python tests/test_syntax_and_imports.py
```

## What Gets Tested

- **Syntax validation** - Ensures all Python files parse correctly
- **Python 3 compatibility** - Checks for Python 2 print statements
- **Code quality** - Warns about old-style string formatting

## Test Output

Tests provide detailed output showing:
- Files tested
- Pass/fail status for each check
- Specific line numbers for issues found
- Summary statistics

All tests should pass before committing changes.
