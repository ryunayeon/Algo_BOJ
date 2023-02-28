n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input().split()))   # 국어, 영어, 수학 순
arr.sort(key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))   # -국, +영, -수, +이름

for name in arr:
    print(name[0], end='\n')