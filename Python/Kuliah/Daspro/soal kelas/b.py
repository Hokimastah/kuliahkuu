a = int(input())
b = a + 1
c = []
for i in range(1, b):
    if i %2 == 0:
        c.append(i)

d = []
for i in c :
    d.append(str(i))

hasil_akhir = " ".join(d)
print(hasil_akhir)