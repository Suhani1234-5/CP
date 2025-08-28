# LeetCode 14. Longest Common Prefix

## Problem
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

### Example
Input:
strs = ["flower","flow","flight"]

Output: "fl"


## Approach
- Sort the array of strings.
- The longest common prefix must be a prefix of both the first and the last string (because they will be most different after sorting).
- Compare characters one by one until they mismatch.

## Complexity
- **Time:** O(n log n + m), where `n` is the number of strings (for sorting) and `m` is the length of the first string.
- **Space:** O(1), using only extra variables.

## Code
See [solution.py](solution.py).
