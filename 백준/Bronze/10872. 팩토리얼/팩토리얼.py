n = int(input())

def Factoral_recursive(n):
    if n <= 1:
        return 1
    return n * Factoral_recursive(n-1)

print(Factoral_recursive(n))