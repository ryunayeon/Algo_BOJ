from itertools import combinations

n = int(input())
num = []
cnt = 0
if n > 1022:
    print(-1)
else:
    for k in range(1, 11):
        for co in (combinations(range(0, 10), k)):
            co = list(co)
            co.sort(reverse=True)
            num.append(int("".join(map(str, co))))
    num.sort()
    print(num[:n+1][-1])