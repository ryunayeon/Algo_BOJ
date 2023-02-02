import itertools

N, M = map(int, input().split())
nums = list(map(int, input().split()))
three = list(itertools.combinations(nums, 3))
# print(three)

sums = []
for i in range(len(three)):
    sums.append(sum(three[i]))

under_M = []
for num in sums:
    if M >= num:
        under_M.append(num)
under_M.sort()
print(under_M[-1])