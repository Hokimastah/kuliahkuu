a = int(input())
def n2(x):
    if x == 0:
        return 1
    elif x%2 == 1:
        return x* n2(x-1)
    else:
        return (x//2)*n2(x-1)

print(n2(a))