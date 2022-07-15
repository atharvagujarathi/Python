def recursion(n):
    if n<=1:
        return n
    return n + recursion(n-1)

n = 7
print(recursion(n))