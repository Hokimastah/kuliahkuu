# Membaca koordinat dari input
Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Px, Py = map(int, input().split())

# Menentukan kuadran dari ketiga titik pengawas
if Ax > 0 and Ay > 0 :
    kuadran_A = 1
elif Ax < 0 and Ay > 0 :
    kuadran_A = 2
kuadran_A = 1 if Ax > 0 and Ay > 0 else 2 if Ax < 0 and Ay > 0 else 3 if Ax < 0 and Ay < 0 else 4
kuadran_B = 1 if Bx > 0 and By > 0 else 2 if Bx < 0 and By > 0 else 3 if Bx < 0 and By < 0 else 4
kuadran_C = 1 if Cx > 0 and Cy > 0 else 2 if Cx < 0 and Cy > 0 else 3 if Cx < 0 and Cy < 0 else 4

# Menentukan kuadran dari Bjarkan
kuadran_P = 1 if Px > 0 and Py > 0 else 2 if Px < 0 and Py > 0 else 3 if Px < 0 and Py < 0 else 4

# Menentukan perintah penangkapan Bjarkan
if kuadran_P == kuadran_A or kuadran_P == kuadran_B or kuadran_P == kuadran_C:
    if (Ax == Bx == Cx and (Py > Ay or Py > By or Py > Cy)) or (Ay == By == Cy and (Px > Ax or Px > Bx or Px > Cx)):
        print(f"TITIK PENGAWAS: kuadran {kuadran_A} {kuadran_B} {kuadran_C}")
        print("KEPUNG BJARKAN!!!, Tapi Dia Tidak Segaris Dengan Kalian")
    else:
        print(f"TITIK PENGAWAS: kuadran {kuadran_A} {kuadran_B} {kuadran_C}")
        print("KEPUNG BJARKAN!!!, Dia Segaris Dengan Kalian")
else:
    print(f"TITIK PENGAWAS: kuadran {kuadran_A} {kuadran_B} {kuadran_C}")
    print("KEJAR BJARKAN!!!, Dia Masih Segaris Dengan Kalian")