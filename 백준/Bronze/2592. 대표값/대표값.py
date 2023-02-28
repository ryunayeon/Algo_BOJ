from collections import Counter

arr = [int(input()) for _ in range(10)]
av = int(sum(arr) // 10)
val = Counter(arr).most_common()
print(av)
print(val[0][0])