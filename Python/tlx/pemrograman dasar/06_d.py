x = 0
try:
    while True:
        y = int(input())
        x += y
except EOFError:
    print(x)