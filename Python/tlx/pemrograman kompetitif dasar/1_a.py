seleksi = int(input())
jawaban = []
for i in range(seleksi):
    urutan = []
    m, n = list(map(int,input().split()))
    juara = input()
    for k in range(m):
        peserta = list(map(str,input().split()))
        if not urutan:
            urutan.append(peserta)
        for j,a in enumerate(urutan):
            if int(peserta[3])>int(a[3]):
                urutan.insert(j,peserta)
            elif int(peserta[3])==int(a[3]):
                if int(peserta[2])>int(a[2]):
                    urutan.insert(j,peserta)
                elif int(peserta[2])==int(a[2]):
                    if int(peserta[1])>int(a[1]):
                        urutan.insert(j,peserta)
    for j,a in enumerate(urutan):
        if a[0] == juara:
            if j<=n:
                jawaban.append("YA")
            else: jawaban.append("TIDAK")

for i in jawaban:
    print(i)