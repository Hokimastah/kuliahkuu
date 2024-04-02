def langkah(x,y):
    if x == 1:
        return y
    elif x % 3 == 0:
        return langkah((x/3),(y+1))
    elif x % 2 == 0:
        return langkah((x/2),(y+1))
    else:
        return((x-1),(y+1))
x = int(input())
y = 0
print(langkah(x,y))