import datetime
tgl, bln, thn = map(int,input().split())
if bln == 1 :
    n_bln = 'Januari'
elif bln == 2 :
    n_bln = 'Februari'
elif bln == 3 :
    n_bln = 'Maret'
elif bln == 4 :
    n_bln = 'April'
elif bln == 5 :
    n_bln = 'Mei'
elif bln == 6 :
    n_bln = 'Juni'
elif bln == 7 :
    n_bln = 'Juli'
elif bln == 8 :
    n_bln = 'Agustus'
elif bln == 9 :
    n_bln = 'September'
elif bln == 10 :
    n_bln = 'Oktober'
elif bln == 11 :
    n_bln = 'November'
elif bln == 12 :
    n_bln = 'Desember'

b = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
c = b[datetime.datetime(thn,bln,tgl).weekday()]

print(f'Tanggal : {tgl} {n_bln} {thn} ')
print(f'Hari : {c}')