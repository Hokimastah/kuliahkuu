def kocak(a):
    b = []
    for i in range(a + 1):
        b.append(i)
    for i in range(a):
        b.append(a - (i + 1))
    c = " ".join(map(str, b))
    return c

def spasi(a):
    x = " " * (2 * a)
    return x

a = int(input())
x = a
y = 0

while x >= 0 and y <= a:
    print(spasi(x) + kocak(y))
    x -= 1
    y += 1
    
y -= 2
x += 2

while x <= a and y >= 0:
    print(spasi(x) + kocak(y))
    x += 1
    y -= 1
