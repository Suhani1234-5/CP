# CodeChef 930 - Hoop Jump

## 📝 Problem Statement
You and your friend are playing a game with hoops.  
There are **N hoops** (where N is always odd) arranged in a row.

- You start jumping from the **first hoop**.
- Your friend starts jumping from the **last hoop**.
- Both of you jump **towards the center hoop** (one hoop at a time).

The game ends when you both **land on the same hoop**.  
You need to determine the position of this **meeting hoop**.

---

## 📥 Input
- The first line contains an integer **T** → number of test cases.  
- Each test case contains a single integer **N** → the number of hoops.

---

## 📤 Output
For each test case, print the position (1-indexed) of the **meeting hoop**.

---

## ✅ Example
### Input
2
1
3


### Output


1
2

---

## 🖥️ Solution Code (Python)
```python
# cook your dish here

t = int(input())
for _ in range(t):
    n = int(input())
    print(n // 2 + 1)
yaml
Copy
Edit

