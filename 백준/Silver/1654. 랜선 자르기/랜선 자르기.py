k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

ans = 0  # 랜선의 최대 길이

start, end = 1, max(arr)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in arr:  # mid 길이로 랜선 자름
        cnt += i // mid
    if cnt >= n:  # 랜선의 개수가 n 이상
        start = mid + 1
        ans = mid
    else:  # 랜선의 개수가 n 미만
        end = mid - 1

print(ans)