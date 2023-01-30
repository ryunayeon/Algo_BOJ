nums = []
for _ in range(10):
    nums.append(int(input()))

r_lst = []
for i in nums:
    r_lst.append(i % 42)
new_lst = list(set(r_lst))
print(len(new_lst))