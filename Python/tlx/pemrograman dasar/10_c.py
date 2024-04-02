def nol(x):
    x = [char for char in x]
    x.reverse()
    for i in x:
        if i == 0:
            x.remove(i)
        else:
            break
    x = "".join(x)
    return int(x)
        
a, b = map(str,input().split())
a = nol(a)
b = nol(b)
c = [char for char in str(a + b)]
c.reverse()
c = int("".join(c))
print(c)