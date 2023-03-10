n, m = map(int, input().split())

lst = set([input() for _ in range(n)])
cnt = 0
for _ in range(m):
    t = input()
    if t in lst:
        cnt += 1

print(cnt)