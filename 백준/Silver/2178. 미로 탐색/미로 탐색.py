def bfs(si, sj):
    q = []
    q.append((si, sj))
    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1:
                    q.append((ni, nj))
                    arr[ni][nj] = arr[ci][cj] + 1
    return arr[n-1][m-1]


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))
print(bfs(0, 0))