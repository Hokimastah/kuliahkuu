a = int(input())
b = list(map(int, input().split()))

c = []

while len(b) > 0:
    x = b.copy()
    d = []
    for i in x:
        if len(d) == 0:
            d.append(i)
            b.remove(i)
            continue
        if d[-1] - 1 == i:
            d.append(i)
            b.remove(i)
        else:
            continue
    c.append(d)

print(len(c))
