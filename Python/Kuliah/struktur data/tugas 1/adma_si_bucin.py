jumlah_barang = int(input())
barang = []
for i in range(jumlah_barang):
    x = list(map(int,input().split()))
    if not barang:
        barang.append(x)
    else :
        for k in barang:
            if k[1] < x[1]:
                continue
            elif k[1] > x[1]:
                barang.insert(barang.index(k),x)
                break
            else : barang.append(x)
cari = int(input())
y = 0
for i in barang:
    if i[0] == cari:
        print(y)
    elif i[0] != cari:
        y += 1
if y == len(barang):
    print("Barangnya gak ada beb")