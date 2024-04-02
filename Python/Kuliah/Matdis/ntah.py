# a) if x + 2 = 3 then x := x + 1
"""output = 2
        -soal menjelaskan bahwa x = 1
        -kondisi percabangan x + 2 = 3 setelah dimasukan x = 1 menjadi True
        -program akan mengeksekusi nilai x = 1 ke x := x + 1 
        -hasil x = 2
        """
# b) if (x + 1 = 3) OR (2x + 2 = 3) then x := x + 1
"""program tidak akan mengeluarkan hasil, karena kedua pernyataan di atas bernilai false.
        """
# c) if (2x + 3 = 5) AND (3x + 4 = 7) then x := x + 1
"""output = 2
        -soal menjelaskan bahwa x = 1
        -kondisi kedua percabangan setelah dimasukan x = 1 menjadi True
        -program akan mengeksekusi nilai x = 1 ke x := x + 1 
        """
# d) if (x + 1 = 2) XOR (x + 2 = 3) then x := x + 1
"""program tidak akan menampilkan hasil, walaupun kedua kondisi bernilai True, tetapi operator Xor(Exclusive Disjunction)
        ini hanya akan bernilai True jika salah satu dari kedua pernyataan bernilai True.
        """
# e) if x < 2 then x := x + 1
"""hasil dari program adalah 2, karena pernyataan di atas bernilai benar, bahwa x = 1 bernilai lebih kecil dari pada 2
        sehingga program akan di eksekusi dan menampilkan angka 2 sebahai hasil.
        """
