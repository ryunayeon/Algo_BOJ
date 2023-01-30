nums = []
for _ in range(9):
    nums.append(int(input()))
for idx, num in enumerate(nums):
    if num == max(nums):
        print(f'{num}\n{idx+1}')