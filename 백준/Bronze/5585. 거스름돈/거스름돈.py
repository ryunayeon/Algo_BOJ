M = 1000 - int(input())

change = [500, 100, 50, 10, 5, 1]
cnt = 0
for coin in change:
    cnt += M // coin
    M %= coin

print(cnt)