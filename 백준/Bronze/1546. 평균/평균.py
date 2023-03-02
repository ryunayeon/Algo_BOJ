n = int(input())
arr = list(map(int, input().split()))
m = max(arr)
av = 0
for sc in arr:
    av += sc / m * 100
print(av/n)
