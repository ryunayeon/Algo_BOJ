n, m = map(int, input().split())
lst = list(map(int, input().split()))

s = 0
e = max(lst)

result = 0
while s <= e:
    total = 0
    mid = (s + e) // 2
    for x in lst:
        if x > mid:
            total += x - mid
    if total < m:
        e = mid - 1
    else:
        result = mid
        s = mid + 1

print(result)