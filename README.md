# Quick-Calc

Quick-Calc is a lightweight calculator application that supports the four basic arithmetic operations (addition, subtraction, multiplication, division), plus a clear/reset behavior.  
The focus of this project is software quality: clean, testable code and a multi-layered test strategy (unit + integration) managed with Git and GitHub.

## Features
- Addition, subtraction, multiplication, division
- Graceful handling of division by zero (returns `ERROR` in CLI; raises an exception in core logic)
- CLI one-shot mode: `py -m quickcalc.cli 5 + 3`
- Interactive mode: `py -m quickcalc.cli` (type expressions or `C`, `q`)

## Project Structure