n = int(input())
arr = []
for _ in range(n):
    age, name = input().split()
    arr.append((age, name, _+1))

arr.sort(key=lambda x : [int(x[0]), x[2]])
for lst in arr:
    print(lst[0], lst[1], end='\n')