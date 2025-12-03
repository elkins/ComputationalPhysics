# ComputationalPhysics

A survey of computational physics problems in Python. Includes quantum mechanics, electrostatics, ODEs, PDEs, Monte Carlo, Fourier analysis, molecular modeling, cluster growth, genetic algorithms, dynamical systems and more.

**Note**: This codebase has been modernized to Python 3 with comprehensive testing.

## Repository Structure

```
ComputationalPhysics/
├── phys510/          # PHYS 510 course materials
├── phys613/          # PHYS 613 course materials
│   ├── assignments/  # Weekly assignments (A1-A11)
│   └── projects/     # Major course projects (1-4)
├── clusters/         # Cluster growth simulations
├── examples/         # Example programs and utilities
└── tests/            # Automated test suite
```

## Topics Covered

- **Quantum Mechanics**: Finite/infinite square wells, wavefunctions
- **Numerical Methods**: Root finding, integration, differentiation, curve fitting
- **Differential Equations**: ODEs (RK4, RKF45), PDEs (heat, wave equations)
- **Fourier Analysis**: FFT, frequency domain processing
- **Monte Carlo**: Random walks, molecular dynamics
- **Optimization**: Genetic algorithms, conjugate gradient methods
- **Statistical Physics**: Cluster growth (DLA, Eden, percolation), fractals
- **Dynamical Systems**: Van der Pol oscillator, Duffing oscillator, chaos

## Requirements

- Python 3.7+
- NumPy
- Matplotlib
- SciPy (for some examples)

## Testing

Run the test suite to verify all files:
```bash
python tests/test_syntax_and_imports.py
```

## Modernization

This codebase was modernized from Python 2 to Python 3 with the following improvements:
- All `print` statements converted to `print()` functions
- Modern f-string formatting throughout
- Pythonic idioms (e.g., `np.sqrt()` instead of `**0.5`)
- Consistent NumPy usage for mathematical operations
- Automated test suite for ongoing validation

