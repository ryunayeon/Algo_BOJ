n = int(input())
weights = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

weights.sort(reverse=True)
box.sort(reverse=True)
t = 0

if max(box) > max(weights):
    print(-1)
else:
    while len(box) > 0:
        t += 1
        for i in range(n):
            for j in range(len(box)):
                if weights[i] >= box[j]:
                    box.pop(j)
                    break
    print(t)