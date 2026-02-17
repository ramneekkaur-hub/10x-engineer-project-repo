# Project Standards

## Coding Standards
- Follow PEP 8 style guidelines for Python.
- Use type hints for all function parameters and return values.
- Keep functions under 20–25 lines when possible.
- Use descriptive variable and function names.
- Avoid duplicated logic (DRY principle).
- Prefer readability over cleverness.

## Preferred Patterns and Conventions
- Use list comprehensions for creating lists over map or filter functions whenever possible.
- Use f-strings for formatting strings in Python 3.6+.
- Organize imports in the order: standard libraries, third-party libraries, and local imports.

## File Naming Conventions
- Files should be named using lowercase letters with words separated by underscores (snake_case).
- Test files should have the same name as their target file, with `_test` appended.

## Error Handling Approach
- Use try/except blocks to handle exceptions gracefully.
- Log errors with proper context to assist in debugging.
- Always clean up resources (files, network connections, etc.) by using context managers or finally blocks.
- Prefer specific exception types over catching general exceptions.

## Testing Requirements
- All new features must be accompanied by unit tests with a minimum of 80% code coverage.
- Use pytest for testing.
- Ensure all tests are runnable using a single test command.
- Mock external services and dependencies in tests to ensure they're isolated.
- Write clear and descriptive test method names and docstrings.