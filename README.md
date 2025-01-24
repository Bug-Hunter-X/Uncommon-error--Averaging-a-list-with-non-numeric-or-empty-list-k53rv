# Python Code Bug: Averaging a List

This repository contains a Python code example demonstrating a common error in handling list averaging scenarios. The original code lacks error handling for empty lists and non-numeric data types. A solution is provided to address these shortcomings, improving the code's robustness.

## Original Code (bug.py)

The `bug.py` file contains the original code with the error. It attempts to calculate the average of a list but fails if the list is empty or contains non-numeric values.

## Solution (bugSolution.py)

The `bugSolution.py` file provides a corrected version. It uses exception handling and input validation to gracefully manage empty lists and non-numeric data, making the code more resilient.

## How to Run

1. Clone this repository.
2. Navigate to the repository directory.
3. Execute the Python scripts using a Python interpreter: `python bug.py` and `python bugSolution.py`.