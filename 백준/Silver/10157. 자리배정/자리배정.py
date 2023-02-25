c, r = map(int, input().split())
k = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
arr = [[0] * r for _ in range(c)]
# print(arr)
i = j = dr = 0
for cnt in range(1, c * r + 1):
    arr[i][j] = cnt
    ni, nj = i + di[dr], j + dj[dr]

    if 0 <= ni < c and 0 <= nj < r and arr[ni][nj] == 0:
        i, j = ni, nj
    else:
        dr = (dr + 1) % 4
        i, j = i + di[dr], j + dj[dr]

if k <= c * r:
    for lst in arr:
        if k in lst:
            print(arr.index(lst)+1, lst.index(k)+1)
else:
    print(0)