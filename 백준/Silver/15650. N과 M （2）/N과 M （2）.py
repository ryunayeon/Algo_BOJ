from itertools import combinations
n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]

lst = list(combinations(arr, m))
for k in lst:
    print(*k, end='\n')