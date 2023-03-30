n, m = map(int, input().split())

a = {}
for _ in range(n):
    site, pw = input().split()
    a[site] = pw


for _ in range(m):
    print(a[input()])