# Coding_Excercises_Python

Small Python exercises used to practise clean, tested code: algorithm problems,
pytest, and a context manager with logging.

## Files

| File | Purpose |
|---|---|
| `solutions.py` | Solutions to LeetCode #1 (`two_sum`) and #347 (`top_k_frequent`), with type hints, docstrings and complexity notes. |
| `test_solutions.py` | pytest tests for `solutions.py`: parametrized cases with readable ids, edge cases, and `pytest.raises` for the error path. Also contains the `AuditLog` tests. |
| `audit.py` | `AuditLog`, a class-based context manager that logs START and END, or FAILED if the block raises, without suppressing the exception. Uses the `logging` module. |
| `Jupyter_Notebooks/` | Original exploratory notebooks for each problem, before the code moved into `solutions.py`. |
| `requirements.txt` | Pinned dependencies (pytest and its dependencies). |
| `.gitignore` | Excludes `.venv/`, caches and log files. |

## Concepts demonstrated

- **Algorithms:** hash-map `two_sum` in O(n), top-k frequent elements with `Counter`.
- **Testing:** Arrange/Act/Assert, parametrization, edge cases, expected-exception tests, and checking that tests fail when the code is deliberately broken.
- **Context managers:** the `__enter__`/`__exit__` protocol and why `__exit__` should not swallow exceptions.
- **Logging:** emitting records at the correct level, and verifying them with pytest's `caplog` fixture.
- **Tooling:** virtual environment, git commits in small steps.

## Running the tests

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```