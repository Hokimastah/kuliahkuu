s = [char for char in input()]
besar = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
kecil = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
hasil = []
for i in s:
    if besar.count(i) == 1:
        hasil.append(kecil[besar.index(i)])
    else :
        hasil.append(besar[kecil.index(i)])

hasil = "".join(hasil)
print(hasil)