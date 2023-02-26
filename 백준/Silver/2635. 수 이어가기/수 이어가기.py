n = int(input())
maxlen = []
for k in range(1, n+1):
    lst = [n]
    lst.append(k)
    idx = 0
    while True:
        next = lst[idx] - lst[idx+1]
        if next < 0:
            break
        lst.append(next)
        idx += 1
    if len(lst) > len(maxlen):
        maxlen = lst
print(len(maxlen))
print(*maxlen)