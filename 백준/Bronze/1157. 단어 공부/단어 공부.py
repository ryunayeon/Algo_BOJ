lst = input().upper()
set1 = set(lst)
cnt = []
for i in set1:
    cnt.append(lst.count(i))

if cnt.count(max(cnt)) != 1:
    print('?')
else:
    print(list(set1)[cnt.index(max(cnt))])