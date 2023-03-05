n, m, b = map(int, input().split())
arr = []
for _ in range(n):
    arr += list(map(int, input().split()))
arr.sort(reverse=True)
minV = min(arr)
maxV = max(arr)
cnt = -1
hei = 0
for i in range(minV, maxV + 1):
    t = 0
    k = b
    for j in arr:
        if j < i:
            t += i - j
            k -= i - j
        elif j > i:
            t += (j - i) * 2
            k += j - i
    if k < 0:
        break
    if cnt == -1 or t <= cnt:
        cnt = t
        hei = i
print(cnt, hei)