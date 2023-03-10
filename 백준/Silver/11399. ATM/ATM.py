n = int(input())
arr = list(map(int, input().split()))
arr.sort()
sum_lst = [arr[0]]
for i in range(n-1):
    sum_lst.append(sum_lst[i] + arr[i+1])
print(sum(sum_lst))