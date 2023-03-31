def dfs(i, sm):
    global ans

    if i >= n:
        return
    
    sm += lst[i]
    
    if sm == k:
        ans += 1
    # [2] 하부
    # 포함
    dfs(i+1, sm)
    # 불포함
    dfs(i+1, sm - lst[i])

n, k = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0
dfs(0, 0)

print(ans)