n, m = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))

# print(money)
s = min(money)
e = sum(money)
while s <= e:
    mid = (s + e) // 2
    now = mid   # 지금 뽑아서 갖고 있는 돈
    cnt = 1 # 뽑은 횟수
    for x in money:
        if now < x: # 갖고 있는 돈이 부족하면 돈 또 뽑기
            now = mid
            cnt += 1
        now -= x
    if cnt > m or mid < max(money):  # 너무 자주 뽑았음 -> 인출 금액을 늘려야 함
        # 인출한 돈이 하루에 필요한 최대 금액보다 적음 -> 인출 금액 늘려야 함
        s = mid + 1
    else:   # 인출 횟수가 적음 -> 인출 금액 줄여야 함
        e = mid - 1
        k = mid
print(k)