n, m = map(int, input().split())
pack = []
k = []
for _ in range(m):
    a, b = map(int, input().split())
    pack.append(a)
    k.append(b)

pack.sort()
k.sort()

t = min(pack[0], 6 * k[0])

bulk = (n // 6) * t
piece = (n % 6) * k[0]

print(min(bulk + piece, (n//6+1) * min(pack)))
