import sys
input = sys.stdin.readline

t = int(input())
k = int(input())
arr = []
for _ in range(k):
    p, n = map(int, input().split())
    arr.append((p, n))

dp = [0] * (t + 1)

dp[0] = 1
for c, cnt in arr:
    for m in range(t, 0, -1):
        for i in range(1, cnt+1):

            if m - c * i >= 0:
                dp[m] += dp[m - c * i]

print(dp[t])