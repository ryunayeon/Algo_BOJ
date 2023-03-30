n, m = map(int, input().split())
dict = {}
for i in range(1, n+1):
    x = input()
    dict[i] = x
    dict[x] = i

for _ in range(m):
    k = input()
    if k.isdigit():
        print(dict[int(k)])
    else:
        print(dict[k])