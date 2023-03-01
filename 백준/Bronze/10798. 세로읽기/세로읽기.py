arr = []
for _ in range(5):
    arr.append(list(input()))

k = []
for lst in arr:
    k.append(int(len(lst)))
for lst in arr:
    while len(lst) != max(k):
        lst.append('*')
new = list(map(list, zip(*arr)))
word = ''
for x in new:
    for y in x:
        if y == '*':
            continue
        else:
            word += y
print(word)