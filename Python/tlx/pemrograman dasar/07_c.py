a = int(input())
x = 0
b = list(range(1,a+1))
for i in b:
    angka = []
    for j in range(i):
        angka.append(str(x))
        x+=1
        x%=10
    hasil = "".join(angka)
    print(hasil)