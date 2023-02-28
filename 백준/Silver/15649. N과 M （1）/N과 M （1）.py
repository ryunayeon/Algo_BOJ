from itertools import permutations

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]

lst = list(permutations(arr, m))
for k in lst:
    print(*k, end='\n')