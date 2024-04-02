l, m, k = map(int,input().split())

def pangkat(a,b):
    x = b
    for i in range(a-1):
        x*=b
    return x
x = pangkat(l,m)
for i in range(m+1,k+1):
    x += pangkat(l,i)
    
print(x)