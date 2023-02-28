from collections import Counter

n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
val = Counter(arr).most_common()
val.sort(key=lambda x : (-x[1], x[0]))
print(val[0][0])