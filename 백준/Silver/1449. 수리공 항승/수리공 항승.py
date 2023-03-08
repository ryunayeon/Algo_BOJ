n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0
where = 0
for k in arr:
    if where < k:
        cnt += 1
        where = k + l - 1
print(cnt)