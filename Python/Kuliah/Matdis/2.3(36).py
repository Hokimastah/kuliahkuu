def f(x):
    y = x*x + 1
    return y
def g(x):
    y = x + 2
    return y

def fog(x):
    return f(g(x))
def gof(x):
    return g(f(x))

x = int(input())

print(fog(x))
print(gof(x))