import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

sum_lst = [0]
temp = 0
for k in arr:
    temp += k
    sum_lst.append(temp)

for _ in range(m):
    i, j = map(int, input().split())
    print(sum_lst[j] - sum_lst[i-1])