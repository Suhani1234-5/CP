# Vaccine Dates (CodeChef)

## Problem Statement
Chef has taken his first dose of vaccine D days ago. He may take the second dose no less than L days and no more than R days since his first dose.

Determine if Chef is too early, too late, or in the correct range for taking his second dose.

---

## Input Format
- First line will contain T, number of test cases.
- Each testcase contains three integers D, L, and R.

## Output Format
For each test case, print:
- "Too Early" if D < L
- "Too Late" if D > R
- "Take second dose now" if L <= D <= R

---

## Example
**Input**
3
2 4 8
8 6 8
10 2 6

**Output**
Too Early
Take second dose now
Too Late