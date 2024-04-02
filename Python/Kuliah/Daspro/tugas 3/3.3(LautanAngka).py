a = int(input())
b = list(map(int, input().split()))

def biner(x):
    sisa = x
    hasil = []
    while True :
        hasil.append(sisa % 2)
        sisa //= 2
        if sisa == 0: break
    return hasil

total1 = []
for i in b :
    c = biner(i)
    d = c.count(1)
    total1.append(d)
    
total = sum(total1)
print (total)