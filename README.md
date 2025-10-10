## Example Unit Testing in Python with pytest

This repository contains example code for unit testing in Python using the `pytest`
framework. The examples demonstrate how to write and run unit tests for various
functions and classes.

### Prerequisites
- Python 3.x
- pytest library (install via pip: `pip install pytest`)

### pytest Features
- Simple and easy-to-read syntax
- Automatic test discovery
- Fixtures for setup and teardown
- Support for parameterized tests
- Rich plugin architecture

### pytest In Operation
When you have a test file (e.g., `test_example.py`), you can run the tests using the
command:
```bash
pytest test_example.py -v
```
or you can simply run:
```bash
pytest -v
```
and pytest will automatically discover and run all test functions prefixed
with `test_` or suffixed with `_test.py`. The `-v` flag stands for verbose mode,
which provides more detailed output.

If you use an IDE like PyCharm, you can also run tests directly from the IDE.
If you press 'run' on a test function or class, PyCharm will execute the tests
using pytest and display the results in a dedicated test runner window.

run_tests.sh is also provided to run all tests in the repository. This is a simple
bash script that you can execute in a Unix-like environment. It is optional and
provided for convenience. To run it, make the file executable:
```bash
chmod +x run_tests.sh
```

then use the command:
```bash
bash run_tests.sh
```

### Code Files
- `math_utils.py`: Contains example math functions to be tested.
- `bank_account.py`: Contains a simple BankAccount class to be tested.

### Test Files
- `test_math_utils.py`: Contains example unit tests for various math functions.
- `test_bank_account.py`: Contains example unit tests for a simple BankAccount class.
- `test_bank_account_mocked.py`: Contains example unit tests for the BankAccount class
  using mocking to simulate external dependencies.

### "missing" main function

Note the lack of a `main` function. This is because pytest automatically discovers
and runs test functions without needing a main entry point. We don't main function
because we are not building a standalone application; instead, we are creating
a suite of tests that can be executed independently on individual functions and classes.
This is common practice in unit testing to keep tests modular and focused on specific
units of code.