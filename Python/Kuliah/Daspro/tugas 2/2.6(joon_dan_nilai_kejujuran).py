def is_palindrome(num):
    # Fungsi ini memeriksa apakah suatu bilangan adalah palindrom atau bukan
    return str(num) == str(num)[::-1]

def find_next_palindrome(input_num):
    num = input_num + 1
    while True:
        if is_palindrome(num):
            return num
        num += 1

input_num = int(input("Masukkan nilai input: "))
next_palindrome = find_next_palindrome(input_num)
print(f"Bilangan palindrom berikutnya yang lebih besar dari {input_num} adalah: {next_palindrome}")


"""
Program di atas adalah program Python yang mencari bilangan palindrom yang lebih besar dari nilai yang dimasukkan oleh pengguna. Berikut adalah penjelasan lebih rinci tentang bagaimana program ini berfungsi:

def is_palindrome(num):: Ini adalah fungsi yang memeriksa apakah suatu bilangan adalah palindrom atau tidak. Fungsi ini mengambil satu argumen, yaitu num, dan mengembalikan True jika num adalah palindrom (artinya, bilangan tersebut dapat dibaca sama dari depan maupun dari belakang), dan False jika tidak.

def find_next_palindrome(input_num):: Ini adalah fungsi yang mencari bilangan palindrom berikutnya yang lebih besar dari nilai yang diinputkan oleh pengguna. Fungsi ini mengambil satu argumen, yaitu input_num, yang merupakan nilai yang dimasukkan oleh pengguna.

Program utama dimulai dengan meminta pengguna untuk memasukkan nilai dengan pernyataan input_num = int(input("Masukkan nilai input: ")). Nilai ini akan digunakan sebagai titik awal untuk mencari bilangan palindrom yang lebih besar.

Kemudian, program memanggil fungsi find_next_palindrome(input_num) untuk mencari bilangan palindrom berikutnya yang lebih besar dari input_num.

Dalam fungsi find_next_palindrome, kami menggunakan loop while True untuk terus mencoba bilangan selanjutnya sampai kami menemukan bilangan palindrom.

Dalam setiap iterasi loop, kami memeriksa apakah bilangan saat ini (num) adalah palindrom menggunakan fungsi is_palindrome(num). Jika num adalah palindrom, kami mengembalikan num sebagai hasil.

Jika num bukan palindrom, kami menambahkan 1 ke num dan mengulangi proses pencarian hingga menemukan bilangan palindrom yang sesuai.

Setelah menemukan bilangan palindrom yang lebih besar, program mencetak hasilnya dengan pernyataan print."""