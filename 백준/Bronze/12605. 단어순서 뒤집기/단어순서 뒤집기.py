t = int(input())
for case in range(1, t+1):
    arr = list(input().split())
    print(f'Case #{case}:', *arr[::-1])