# Palindrome Check in Python
In this assignment, you'll design and implement one of the string manipulation functions that is commonly asked during interviews.

## Exercise
* Design and implement a function that checks if the input string is a palindrome. The function should return `True` if the input string is a palindrome, and return `False` if it is not a palindrome.
* Share and explain the time and space complexities for your solution.
* At minimum, your implementation should pass the basic tests.

**Note 1**: A palindrome is a word, phrase or sentence that reads the same backwards as it does forwards. e.g. "madam"

**Note 2**: Do not use Python provided functionality for `reversed()`, `reverse()`, or string slicing (`"string"[::-1]`). You may use `len()`.

## Running the Tests
Install `pytest`
```terminal
pip install pytest
```
To run all tests, navigate to the same directory as the test file and run:
```terminal
pytest test_palindrome_check.py
```
Alternatively, to exit instantly on first error or failed test, run:
```terminal
pytest -x test_palindrome_check.py
```

See [pytest documentation](http://pytest.org/latest/) for more information about `pytest`.
