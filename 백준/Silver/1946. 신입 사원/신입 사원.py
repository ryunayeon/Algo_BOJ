t = int(input())

for tc in range(t):
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(tuple(map(int, input().split())))

    lst.sort(key=lambda x : x[0])
    # print(lst)
    person = 1
    k = lst[0][1]
    for i in range(1, len(lst)):
        if k > lst[i][1]:
            person += 1
            k = lst[i][1]

    print(person)


