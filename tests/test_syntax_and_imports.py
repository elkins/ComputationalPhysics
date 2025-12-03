"""
Smoke tests for ComputationalPhysics codebase
Tests that all Python files have valid syntax and can be parsed
"""
import ast
import sys
from pathlib import Path


def test_file_syntax(filepath):
    """Test that a Python file has valid syntax"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            source = f.read()
        ast.parse(source)
        return True, None
    except SyntaxError as e:
        return False, f"SyntaxError: {e}"
    except Exception as e:
        return False, f"Error: {e}"


def test_python3_print_statements(filepath):
    """Check that file doesn't have Python 2 print statements"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Look for obvious Python 2 print patterns
        issues = []
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            # Skip comments and empty lines
            if not stripped or stripped.startswith('#'):
                continue
            # Look for print without parentheses (heuristic)
            if stripped.startswith("print ") and not stripped.startswith("print("):
                # Check it's not a comment after code
                code_part = line.split('#')[0]
                if code_part.strip().startswith("print "):
                    issues.append(f"Line {i}")
        
        if issues:
            return False, f"Possible Python 2 print on lines: {', '.join(issues)}"
        return True, None
    except Exception as e:
        return False, f"Error: {e}"


def test_no_old_string_formatting(filepath):
    """Check for old-style % string formatting in common patterns"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        issues = []
        for i, line in enumerate(lines, 1):
            # Skip comments
            if line.strip().startswith('#'):
                continue
            # Look for obvious % formatting patterns
            if "print" in line and "'%" in line and "%" in line.split("'%")[1].split("'")[0]:
                issues.append(f"Line {i}: Possible old-style formatting")
        
        if issues:
            return False, "; ".join(issues)
        return True, None
    except Exception as e:
        return False, f"Error: {e}"


def run_tests():
    """Run all tests on Python files in the repository"""
    repo_path = Path(__file__).parent.parent
    
    # Find all Python files recursively
    python_files = []
    for pattern in ["**/*.py"]:
        python_files.extend(repo_path.glob(pattern))
    
    # Exclude test files and hidden directories
    python_files = [f for f in python_files 
                    if f.name != "test_syntax_and_imports.py" 
                    and not any(part.startswith('.') for part in f.parts)]
    
    if not python_files:
        print("No Python files found!")
        return False
    
    print(f"Found {len(python_files)} Python files to test\n")
    print("="*70)
    
    all_passed = True
    failed_tests = []
    
    for py_file in sorted(python_files):
        relative_path = py_file.relative_to(repo_path)
        print(f"\nTesting: {relative_path}")
        print("-" * 70)
        
        file_passed = True
        
        # Test 1: Valid syntax
        passed, error = test_file_syntax(py_file)
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"  Syntax validation: {status}")
        if not passed:
            print(f"    {error}")
            file_passed = False
        
        # Test 2: No Python 2 print statements
        passed, error = test_python3_print_statements(py_file)
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"  Python 3 print():  {status}")
        if not passed:
            print(f"    {error}")
            file_passed = False
        
        # Test 3: Check for old-style formatting (informational)
        passed, error = test_no_old_string_formatting(py_file)
        status = "✓ PASS" if passed else "⚠ WARN"
        print(f"  Modern formatting: {status}")
        if not passed:
            print(f"    {error}")
        
        if not file_passed:
            all_passed = False
            failed_tests.append(str(relative_path))
    
    print("\n" + "="*70)
    print("\nTEST SUMMARY")
    print("="*70)
    print(f"Total files tested: {len(python_files)}")
    print(f"Passed: {len(python_files) - len(failed_tests)}")
    print(f"Failed: {len(failed_tests)}")
    
    if failed_tests:
        print("\nFailed files:")
        for fname in failed_tests:
            print(f"  - {fname}")
    else:
        print("\n✓ All tests passed!")
    
    return all_passed


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
