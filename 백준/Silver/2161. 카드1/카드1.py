from collections import deque

n = int(input())
d = deque([i for i in range(1, n+1)])
remain = []
while len(d) > 1:
    a = d.popleft()
    remain.append(a)
    k = d.popleft()
    d.append(k)

print(*remain, d[0])