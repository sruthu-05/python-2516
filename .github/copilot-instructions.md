# Copilot Instructions for python-2516

## Project Overview
This workspace is a collection of Python scripts and exercises focused on basic programming concepts, control flow, string manipulation, and simple business logic (e.g., tuition fee and EMI calculations). There is no central application or package structure; each folder contains standalone scripts for specific topics.

## Directory Structure & Key Files
- `01_basics/` — Arithmetic and variable basics
- `04_strings/demo.py` — String operations, slicing, immutability, and edge cases
- `data_types_05/data_types/` — Control flow, loops, match-case, input handling
- `mahindra_car_EMI/` — Business logic for car EMI and student fee calculations
- `interpolation.py` — String interpolation examples
- `myntra.py` — Tuition fee calculation with match-case and input validation
- `README.md` — Contains example code and variable usage, not build/test instructions

## Developer Workflows
- **No build system or test framework is present.**
- Run scripts directly using `python <scriptname.py>` in PowerShell.
- Scripts often require user input; automation is limited.
- No external dependencies or requirements.txt detected.

## Coding Patterns & Conventions
- **Procedural style:** Each script is self-contained, using global variables and direct input/output.
- **Input validation:** Common in business logic scripts (e.g., grade level checks in `myntra.py` and `student_fees`).
- **Match-case:** Used for control flow in Python 3.10+ (see `match_case_demo.py`, `myntra.py`).
- **String handling:** Demonstrates slicing, immutability, and edge cases (see `demo.py`).
- **Loops:** Both `for` and `while` loops are used for iteration and input validation.
- **Error handling:** Minimal; most scripts print error messages rather than raising exceptions.
- **Comments:** Used to explain logic and edge cases, especially in educational scripts.

## Integration Points
- No external APIs, packages, or data files are referenced.
- All scripts are standalone and do not import from each other.

## Examples
- **String slicing:** `text[::-1]` for reversal, `text[1:4:-1]` for edge case demonstration.
- **Match-case:**
  ```python
  match grade_level:
      case 10:
          discount_percentage += 3
      case 12:
          discount_percentage += 5
  ```
- **Input validation:**
  ```python
  if grade_level < 1 or grade_level > 12:
      print("error: grade level must be between 1 and 12.")
  ```

## Recommendations for AI Agents
- Focus on script-level improvements, input validation, and clear output formatting.
- When adding new scripts, follow the procedural style and comment conventions.
- If introducing tests or automation, create a new folder and document the workflow in README.md.
- For new business logic, reference `myntra.py` and `student_fees` for input validation and summary output patterns.

---
**Feedback requested:**
- Are there any workflows, conventions, or integration points that need more detail?
- Is there a plan to add tests, requirements, or a build system?
