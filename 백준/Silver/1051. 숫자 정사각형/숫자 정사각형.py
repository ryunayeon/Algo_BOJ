n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(input()))
sq = []
for i in range(n):
    for j in range(m):
        num = arr[i][j]
        for k in range(j, m):
            if arr[i][k] == num and i+k-j < n:
                if arr[i+k-j][j] == num and arr[i+k-j][k] == num:
                    sq.append((k-j+1)**2)
print(max(sq))