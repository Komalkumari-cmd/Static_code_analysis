| Issue Type | Tool | Line(s) | Description | Fix Approach |
|-------------|-------|----------|--------------|----------------|
| Mutable default argument | Pylint | 8 | `logs=[]` created a shared list across calls | Changed default to `None` and initialized inside |
| Broad exception | Bandit / Pylint | 19 | `except:` hides real bugs | Replaced with `except KeyError:` |
| Dangerous function usage | Bandit | 59 | `eval()` allows arbitrary code execution | Removed `eval()` |
| File handling | Bandit | 26, 32 | `open()` used without encoding or context manager | Used `with open(..., encoding="utf-8")` |
| Missing docstrings | Pylint | Multiple | Functions lacked documentation | Added descriptive one-line docstrings |
