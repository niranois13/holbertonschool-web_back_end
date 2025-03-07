# Unit Tests and Integration Tests


![unittest_integration_tests](https://i.imgur.com/G5mxumZ.png)

- [Unit Tests and Integration Tests](#unit-tests-and-integration-tests)
  - [Unit Tests](#unit-tests)
    - [What are Unit Tests?](#what-are-unit-tests)
    - [Key Characteristics:](#key-characteristics)
    - [Example:](#example)
  - [Integration Tests](#integration-tests)
    - [What are Integration Tests?](#what-are-integration-tests)
    - [Key Characteristics:](#key-characteristics-1)
    - [Example:](#example-1)

## Unit Tests

### What are Unit Tests?
Unit tests focus on testing individual functions or small units of code in isolation. The goal is to ensure that a function behaves correctly given a variety of inputs, including standard cases and edge cases.

### Key Characteristics:
- Tests a single function or method.
- Mocks external dependencies (e.g., database calls, API requests).
- Focuses on expected outputs for given inputs.
- Ensures logic inside the function works correctly.

### Example:
```
import unittest
from my_module import add_numbers

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)
    
    def test_add_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
```

## Integration Tests

### What are Integration Tests?
Integration tests validate the interactions between multiple components of a system. Unlike unit tests, integration tests do not mock most dependencies, ensuring that the system works as expected end-to-end.

### Key Characteristics:
- Tests multiple components working together.
- Only mocks low-level external dependencies (e.g., API calls, file/database I/O).
- Ensures end-to-end behavior is correct.
- Helps detect issues in interactions between modules.

### Example:
```
import unittest
from my_app import create_user, get_user_from_db

class TestUserIntegration(unittest.TestCase):
    def test_create_and_fetch_user(self):
        user_id = create_user("John Doe", "john@example.com")
        user = get_user_from_db(user_id)
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "john@example.com")

if __name__ == '__main__':
    unittest.main()
```

Both types of tests are essential to ensure software reliability and maintainability. Unit tests help catch small bugs early, while integration tests verify that everything works together as expected.