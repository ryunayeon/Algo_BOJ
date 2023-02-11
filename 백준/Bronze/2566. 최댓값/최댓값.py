arr = []
for _ in range(9):
    arr.append(list(map(int, input().split())))

maxV = -1
x = 0
y = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] > maxV:
            x = i + 1
            y = j + 1
            maxV = arr[i][j]
print(maxV)
print(x, y)

