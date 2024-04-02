def cn(n):
    if n == 1:
        return 5
    x = 2*cn(n-1) + n
    return x
n = int(input())
print(cn(n))