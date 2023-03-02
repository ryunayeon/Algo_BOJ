n = int(input())
card = sorted(list(map(int, input().split())))
m = int(input())
nums = list(map(int, input().split()))

for k in nums:
    start = 0
    mid = n // 2
    end = n - 1
    while k != card[mid]:
        if end == start:
            print(0, end=' ')
            break
        elif k < card[mid]:
            end = mid - 1
        else:
            start = mid
        mid = (end + start + 1) // 2
    else:
        print(1, end=' ')