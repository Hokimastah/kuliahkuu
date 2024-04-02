def kursi(a,b):
        satu(a,b)
        tiga(a,b)
        lima(a,b)

        return b

def satu(a,b):
    if a==0:
        b+=1
    elif (a-1) >= 0:
        a -=1
        return kursi(a,b)
def tiga(a,b):
    if a==0:
        b+=1
    elif (a-3) >= 0:
        a -=3
        return kursi(a,b)
def lima(a,b):
    if a==0:
        b+=1
    elif (a-5) >= 0:
        a -=5
        return kursi(a,b)

    
c = 0
a = int(input())
b = list(map(int,input().split()))

for i in b :
    x = kursi(i,c)
    print(x)
