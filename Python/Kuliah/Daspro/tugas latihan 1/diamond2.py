tinggi = int(input("Masukkan tinggi segitiga: "))

for i in range(1, tinggi + 1):
    print(" " * (tinggi - i), "*" * (i + i - 1))
    
for i in range(tinggi+1, tinggi*2) :
    print(" " * (i-tinggi), "*" * (tinggi**2 - i*2-tinggi-1))