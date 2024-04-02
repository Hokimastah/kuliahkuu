j = list(map(int,input().split()))
a = j[0]
b = j[1]
z = [1,1]
y = 100-a
if b > a:
    y-=1
x = y    
        
def finish(x,y,z):
    if y==0:
        return
    z.append(sum(z[-6:]))
    y-=1  
    finish(x,y,z)
    return z[x]

i = finish(x,y,z)
if a == 100:
    i = 0
print(f"Ada {i} cara nih!")