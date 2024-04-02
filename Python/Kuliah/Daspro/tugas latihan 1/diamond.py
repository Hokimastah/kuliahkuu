tinggi = int(input("Masukkan tinggi segitiga: "))

for i in range(1, tinggi + 1):
    print(" "*(tinggi-i) + "*"*i +"*"*(i-1))

