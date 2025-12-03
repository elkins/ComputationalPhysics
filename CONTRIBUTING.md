# Contributing to ComputationalPhysics

Thank you for your interest in contributing to this computational physics repository!

## Code Standards

This project follows modern Python 3 best practices:

### Python Version
- **Minimum**: Python 3.7+
- **Recommended**: Python 3.9 or higher

### Code Style
- Follow [PEP 8](https://pep8.org/) style guidelines
- Use **snake_case** for file and function names
- Use **f-strings** for string formatting
- Limit line length to **100 characters** (configured in `.editorconfig` and `pyproject.toml`)

### Formatting Tools
We recommend using these tools (configurations provided in `pyproject.toml`):
- **Black**: Code formatter
- **isort**: Import sorter
- **Pylint**: Code linter (with physics-friendly settings)

```bash
# Install dev dependencies
pip install black isort pylint

# Format code
black .
isort .

# Check code quality
pylint path/to/file.py
```

## Dependencies

### Core Requirements
- NumPy >= 1.21.0
- SciPy >= 1.7.0
- Matplotlib >= 3.4.0

Install with:
```bash
pip install -r requirements.txt
```

## Testing

Before submitting changes, run the test suite:

```bash
python tests/test_syntax_and_imports.py
```

All files must:
- ✅ Pass syntax validation
- ✅ Be Python 3 compatible (no Python 2 print statements)
- ✅ Use modern string formatting (f-strings preferred)

## Matplotlib LaTeX Strings

When using LaTeX in matplotlib labels, **always use raw strings** to avoid escape sequence warnings:

```python
# ✅ Good
plt.xlabel(r'$\omega$')
plt.annotate(r'$f = \exp(-t)$', ...)

# ❌ Bad
plt.xlabel('$\omega$')  # SyntaxWarning: invalid escape sequence
plt.annotate('$f = \exp(-t)$', ...)  # SyntaxWarning
```

## Project Structure

```
ComputationalPhysics/
├── phys510/              # PHYS 510 course materials
├── phys613/              # PHYS 613 course materials
│   ├── assignments/      # Weekly assignments
│   └── projects/         # Major projects
├── clusters/             # Cluster simulations
├── examples/             # Example programs
└── tests/                # Test suite
```

## Adding New Files

1. **Use snake_case naming**: `new_simulation.py` not `New Simulation.py`
2. **Place in appropriate directory**: Match the course or topic structure
3. **Use modern Python 3 syntax**: print functions, f-strings, type hints (optional)
4. **Add to README if significant**: Update relevant directory README
5. **Test your code**: Ensure it passes the test suite

## Pull Request Process

1. **Fork** the repository
2. **Create a branch** for your feature: `git checkout -b feature/new-simulation`
3. **Make your changes** following the code standards
4. **Run tests**: `python tests/test_syntax_and_imports.py`
5. **Commit** with clear messages: `git commit -m "Add quantum tunneling simulation"`
6. **Push** to your fork: `git push origin feature/new-simulation`
7. **Open a Pull Request** with a clear description of your changes

## Commit Message Guidelines

Use clear, descriptive commit messages:

```bash
# Good
git commit -m "Add FFT analysis for harmonic oscillator"
git commit -m "Fix escape sequences in matplotlib labels"
git commit -m "Update dependencies to NumPy 1.24"

# Less helpful
git commit -m "Update file"
git commit -m "Fix bug"
git commit -m "Changes"
```

## Questions?

Feel free to open an issue for:
- Bug reports
- Feature requests
- Questions about the physics or code
- Suggestions for improvements

Thank you for contributing! 🎉
