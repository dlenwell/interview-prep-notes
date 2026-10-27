#problems:

- [Word Pattern](problems/word-pattern/)

#tester:

## `run.sh` — Python Practice Test Runner

A lightweight test runner for practicing Python coding problems with immediate feedback.

The script runs linting and unit tests once, then watches the selected problem directory for changes. Whenever a Python file is saved, it automatically reruns the checks.

### Usage

```bash
./run.sh problems/word-pattern
```

### Requirements

- Python 3 with `unittest` (standard library)
- `ruff` for linting
- `entr` for filesystem monitoring (`brew install entr`)

### Expected directory structure

```text
problems/
  word-pattern/
    solution.py
    test_solution.py
```

### Behavior

1. Runs Ruff against `solution.py` only.
2. Discovers and executes unit tests in the problem directory.
3. Executes `solution.py` directly.
4. Watches for changes to Python files and repeats the process on save.

Test files are intentionally excluded from linting to keep the focus on practicing solution code.

Press `Ctrl+C` to stop watching.