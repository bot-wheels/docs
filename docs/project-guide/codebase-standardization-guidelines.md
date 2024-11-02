# Codebase Standardization Guidelines

## Introduction

To improve code consistency, readability, and facilitate future development, we are introducing a unified concept for standardizing variable naming conventions, code documentation, and file organization across the project.

## Goals

- **Establish a unified variable naming convention.**
- **Define a standard approach to in-code documentation.**
- **Ensure consistency in file structure and function naming across the repository.**

## Naming Conventions

### Variables and Functions

- Use **snake_case** for variable and function names.
  - Example: `user_name`, `calculate_total()`

### Constants

- Use **UPPER_SNAKE_CASE** for constants.
  - Example: `MAX_RETRIES`, `API_ENDPOINT`

### Classes

- Use **PascalCase** (also known as UpperCamelCase) for class names.
  - Example: `UserProfile`, `DataProcessor`

### File Naming

- All file names in the should follow the `bot-wheels-core` repository **snake_case** convention.
  - Example: `user_profile.py`, `data_processor.py`
- For docs we are sticking with **kebab-case**.
  - Example: `codebase-standardization-guidelines.md`, `match-against-ai-bots.md`

## In-Code Documentation

- **Docstrings**:
  - Use triple double-quotes `"""` for module, class, and function/method docstrings.
  - Follow the [PEP 257](https://www.python.org/dev/peps/pep-0257/) conventions.
  - Include descriptions of the function's purpose, arguments, return values, and exceptions.

- **Inline Comments**:
  - Use sparingly to explain non-obvious code.
  - Begin with `#` followed by a space.
  - Place above the code line or at the end if the comment is brief.

### Example of a Function with Docstring

```python
def calculate_total(price, quantity):
    """
    Calculate the total price for a number of items.

    Args:
        price (float): The price of a single item.
        quantity (int): The number of items purchased.

    Returns:
        float: The total price calculated as price multiplied by quantity.
    """
    return price * quantity
```

## File Organization

- **Directory Structure**:
  - Organize files into directories based on features or functionality.
  - Use `__init__.py` files to define Python packages.

- **Module Structure**:
  - Each module should have a clear purpose and contain related classes and functions.
  - Avoid circular dependencies by carefully structuring imports.

## Steps for Implementation

### 1. Review Current Codebase

- **Action**: Conduct a comprehensive review of existing naming conventions, documentation styles, and file organization.
- **Goal**: Identify inconsistencies and areas needing refactoring.

### 2. Concept Development

- **Action**: Create detailed guidelines (this document) for naming, documentation, and file structure.
- **Goal**: Establish clear standards for the team to follow.

### 3. Team Alignment

- **Action**: Present the guidelines to the team for feedback and discussion.
- **Goal**: Achieve consensus and ensure everyone understands the new standards.

### 4. Implementation

- **Action**: Plan and execute the refactoring of existing code according to the new standards.
- **Goal**: Update the codebase to be consistent and maintainable.

## Conclusion

Adopting these standardized conventions will enhance code readability and maintainability, making it easier for all team members to collaborate effectively. Consistency in coding practices is essential for the long-term success of our project.
