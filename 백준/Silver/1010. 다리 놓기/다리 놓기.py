import math

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    k = math.comb(m, n)
    print(k)
