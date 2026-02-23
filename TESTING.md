# Testing Strategy (Quick-Calc)

This document describes the testing approach used for Quick-Calc and links it to key concepts from Lecture 3.

## What we tested

### Unit tests
Unit tests validate the core arithmetic logic in `quickcalc/calculator.py`:

- addition, subtraction, multiplication, division  
- edge cases:
  - division by zero  
  - negative numbers  
  - decimal numbers  
  - very large numbers  

These tests are fast and verify each function in isolation.

### Integration tests
Integration tests verify that the CLI correctly interacts with the calculator logic.

They:

- run the CLI as a subprocess  
- pass user arguments  
- check the printed output  

This ensures the full flow works correctly.

---

## What we did not test (and why)

- **GUI testing**: the project uses a CLI only.
- **Performance testing**: not critical for a simple calculator.
- **Full interactive automation (C and q)**: interactive terminal testing is platform-dependent; instead we verified isolation between runs.

---

## Lecture Concepts

### Testing Pyramid
The project follows the testing pyramid:

- many unit tests (base layer)  
- few integration tests (top layer)  

This provides fast feedback and good coverage.

### Black-box vs White-box testing

- Unit tests → closer to **white-box** (we know internal functions)
- Integration tests → closer to **black-box** (we only check inputs/outputs)

### Functional vs Non-Functional testing

Covered:

- arithmetic correctness  
- error handling  

Not covered:

- performance  
- security  
- usability  

because they are not primary goals for this project.

### Regression Testing

The test suite can be run after any change to detect regressions.  
If a future modification breaks an operation, the tests will fail immediately.

---

## Test Results Summary

| Test name | Type | Status |
|----------|------|--------|
| Core arithmetic tests | Unit | Pass |
| Edge case tests | Unit | Pass |
| CLI addition test | Integration | Pass |
| CLI isolation test | Integration | Pass |