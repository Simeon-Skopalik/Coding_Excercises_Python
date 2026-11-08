# Coding_Excercises_Python

Small Python exercises used to practise clean, tested code: algorithm problems,
pytest, and a context manager with logging.

## Files

| File | Purpose |
|---|---|
| `solutions.py` | `two_sum` (LeetCode #1) and `top_k_frequent` (#347), with type hints and docstrings. |
| `generators.py` | `positive_prices`, a lazy generator that yields positive, finite floats from an iterable of strings and skips blank, non-numeric, non-positive and non-finite lines. |
| `audit.py` | `AuditLog`, a class-based context manager that logs START and END, or FAILED at ERROR level if the block raises. It never suppresses the exception. |
| `test_solutions.py` | All pytest tests: parametrized cases with readable ids, edge cases, `pytest.raises` for the error path, generator behaviour (laziness, single pass) and `caplog` tests for the logging. |
| `Jupyter_Notebooks/` | Original exploratory notebooks, from before the code moved into modules. |
| `requirements.txt` | Pinned dependencies (pytest and its dependencies). |
| `.gitignore` | Excludes `.venv/`, caches and log files. |

## Concepts demonstrated

- **Algorithms:** one-pass hash-map `two_sum` in O(n); top-k frequent with `Counter`.
- **Testing:** Arrange/Act/Assert, parametrization, edge cases, expected exceptions, and checking that each test fails when the code is deliberately broken.
- **Generators:** lazy evaluation, one-pass behaviour, and why `Iterator[float]` is the correct return hint.
- **Context managers:** the `__enter__`/`__exit__` protocol and why `__exit__` should not swallow errors.
- **Logging:** records emitted at the correct level and verified with `caplog`.

## Running the tests

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```