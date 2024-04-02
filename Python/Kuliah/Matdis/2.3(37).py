def f(x):
    y = x*x + 1
    return y
def g(x):
    y = x + 2
    return y

def plus(x):
    y = f(x)+g(x)
    return y
def fg(x):
    y = f(x)*g(x)
    return y

x = int(input())

print(plus(x))
print(fg(x))