n, m = map(int, input().split())
never_heard = set()
nerver_seen = set()
for _ in range(n):
    never_heard.add(input())
for _ in range(m):
    nerver_seen.add(input())

result = sorted(list(never_heard & nerver_seen))
print(len(result))
for x in result:
    print(x)