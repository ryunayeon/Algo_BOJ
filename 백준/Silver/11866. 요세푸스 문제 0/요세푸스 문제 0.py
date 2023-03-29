n, k = map(int, input().split())

arr = [x for x in range(1, n+1)]

ans = []
for i in range(len(arr)):
    if len(arr) > k-1:
        ans.append(arr.pop(k-1))
        arr = arr[k-1:] + arr[:k-1]
    else:
        idx = (k-1) % len(arr)
        ans.append(arr.pop(idx))
        arr = arr[abs(idx):] + arr[:abs(idx)]

print('<', end='')
print(*ans, sep=', ', end='')
print('>')