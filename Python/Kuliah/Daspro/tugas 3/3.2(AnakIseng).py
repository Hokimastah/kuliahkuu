huruf = input()
a = int(input())
y = []
for x in range(a) :
    kata = input()

    arr_hrf = [char for char in huruf]
    arr_kata = [char for char in kata]

    hasil = []
    for i in arr_kata :
        if i in arr_hrf :
            hasil.append(arr_hrf.index(i))
        else : 
            hasil.append(i)
        
    hasil2 = []
    for j in hasil:
        if type(j) == str:
            hasil2.append(j)
        else:
            hasil2.append(arr_hrf[(j + 1) % len(arr_hrf)])

    hasil_akhir = "".join(hasil2)
    y.append(hasil_akhir)

for z in range(y):
    print(z)