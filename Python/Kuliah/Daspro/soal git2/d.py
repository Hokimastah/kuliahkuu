x = list(map(int,input().split()))
a = x[0]
b = x[1]
c = []
def finish(a,b,c):
    if a == 100:
        c.append(1)
        return
    elif a == b or a>100:
        return
    finish(a+1,b,c)
    finish(a+2,b,c)
    finish(a+3,b,c)
    finish(a+4,b,c)
    finish(a+5,b,c)
    finish(a+6,b,c)
    return len(c)

x = finish(a,b,c)
print(f"Ada {x} cara nih!")
