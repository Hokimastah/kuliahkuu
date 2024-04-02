try:
    # Kode yang mungkin menimbulkan pengecualian
    x = int(input("Masukkan sebuah angka: "))
    hasil = 10 / x
    print("Hasil:", hasil)

except ZeroDivisionError:
    # Menangani pengecualian jika terjadi pembagian dengan nol
    print("Error: Tidak bisa dibagi dengan nol.")

except ValueError:
    # Menangani pengecualian jika input tidak valid (bukan bilangan bulat)
    print("Error: Masukkan bilangan bulat yang valid.")

except Exception as e:
    # Menangani pengecualian lainnya
    print("Terjadi kesalahan yang tidak terduga:", e)

else:
    # Blok ini dijalankan jika tidak ada pengecualian yang terjadi dalam blok try
    print("Tidak ada pengecualian yang terjadi.")

finally:
    # Blok ini selalu dijalankan, baik terjadi pengecualian atau tidak
    print("Ini adalah blok finally.")