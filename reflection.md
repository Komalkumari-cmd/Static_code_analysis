### Reflection

**1. Easiest vs Hardest Fixes:**  
Easiest fixes were removing `eval()` and adding specific exception types.  
Hardest was fixing the mutable default argument and adding docstrings consistently.

**2. False Positives:**  
Bandit flagged global variables as potential risks, but in this small local program, they are safe.

**3. Integration in Workflow:**  
These tools (Pylint, Bandit, Flake8) can be integrated into a CI/CD pipeline such as GitHub Actions to automatically check every commit before merging.

**4. Improvements Observed:**  
After applying fixes, the code became cleaner, more secure, and easier to read.  
Proper use of `with open()` and logging improved both reliability and maintainability.
