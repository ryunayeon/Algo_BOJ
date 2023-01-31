A, B = map(int, input().split())

re_A = int(str(A)[::-1])
re_B = int(str(B)[::-1])

if re_A > re_B:
    print(re_A)
elif re_A < re_B:
    print(re_B)
else:
    print(f'{re_A} = {re_B}')