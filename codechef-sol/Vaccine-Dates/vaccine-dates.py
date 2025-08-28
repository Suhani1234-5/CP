## Code
###python
n = int(input())
for _ in range(n):
    D, L, R = map(int, input().split())
    if L <= D <= R:
        print("Take second dose now")
    elif D > R:
14-longest-common-prefix        print("Too Late")
    else:
        print("Too Early")
