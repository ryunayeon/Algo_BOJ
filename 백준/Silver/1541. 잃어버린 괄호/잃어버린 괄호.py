import re

arr = list(input().split('-'))
'''
'-' 다음 '+'에서 괄호 열고 '+' 끝날 때 괄호 닫음
'''
total = 0

if '+' in arr[0]:
    pl = re.findall(r'\d+', arr[0])
    sums = 0
    for j in pl:
        sums += int(j)
    total += sums
else:
    total += int(arr[0])

for k in arr[1:]:
    if '+' in k:
        ans = re.findall(r'\d+', k)
        temp = 0
        for i in ans:
            temp -= int(i)
        total += temp
    else:
        total -= int(k)

print(total)