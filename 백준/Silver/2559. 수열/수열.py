import sys
input = sys.stdin.readline
# sys.stdin = open('2559.txt')

n, k = map(int, input().split())
c = list(map(int, input().split()))

temp = [sum(c[:k])]
for i in range(n-k):
    temp.append(temp[-1] - c[i] + c[i+k])
print(max(temp))