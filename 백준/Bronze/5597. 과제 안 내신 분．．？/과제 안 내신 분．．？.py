nums = []
for _ in range(28):
    nums.append(int(input()))

for i in range(1, 31):
    if i not in nums:
        print(i)
    else:
        continue