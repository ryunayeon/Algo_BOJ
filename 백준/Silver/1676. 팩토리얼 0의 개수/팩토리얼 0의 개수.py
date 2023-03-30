import math

n = int(input())
num = str(math.factorial(n))

# print(str(num))1
cnt = 0
for i in str(num)[::-1]:
    if i != '0':
        break
    cnt += 1

print(cnt)