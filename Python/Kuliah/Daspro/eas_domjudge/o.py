import math

a = list(map(int,input().split()))
b = math.gcd(a[0],a[1])
c = str(b)
d = [char for char in c]
if len(d)%2==0:
    print('Yey brankas berhasil dibuka :D')
else :
    print('Yah gagal :(')