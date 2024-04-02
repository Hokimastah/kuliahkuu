a, b, k, x = map (int,input().split())
def ntah(a,b,k,x,i):
    if k == i:
        return x
    else:
        i+=1
        x = abs((a*x)+b)
        return ntah(a,b,k,x,i)
print(ntah(a,b,k,x,0))