
a = int(input())

if a>25 :
     print ('soalnya cuma 25 bang')
     StopIteration

jam = int(input())
menit = int(input())
detik = int(input())

# waktu pengerjaan
if jam < 10  :
    sisa_jam = (9-jam)
    if sisa_jam == 0 and menit >= 55 :
        sisa_detik = int(detik//60)
        jam_sisa = str(sisa_jam)
        menit_sisa = str(sisa_jam)
        detik_sisa = str(sisa_detik)
    elif sisa_jam == 0 :
         if detik == 0 :
              sisa_menit = int(55 - menit)
              sisa_detik = int(sisa_menit*60 - detik)
              jam_sisa = str(sisa_jam)
              menit_sisa = str(sisa_menit)
              detik_sisax = int(sisa_detik%60)
              detik_sisa = str(detik_sisax)
         else :
               sisa_menit = int(54 - menit)
               sisa_detik = int((sisa_menit +1)*60 - detik)
               jam_sisa = str(sisa_jam)
               menit_sisa = str(sisa_menit)
               detik_sisax = int(sisa_detik%60)
               detik_sisa = str(detik_sisax)       
    elif sisa_jam >0 :
        if menit >= 55 :
             jam_sisax = int(sisa_jam -1)
             if detik == 0 :
                  sisa_menit = int(55 - menit)
                  sisa_detik = int(sisa_menit*60 - detik)
                  jam_sisa = str(sisa_jam)
                  menit_sisa = str(sisa_menit)
                  detik_sisax = int(sisa_detik%60)
                  detik_sisa = str(detik_sisax)
             else :
                  sisa_menit = int(54 - menit)
                  sisa_detik = int((sisa_menit +1)*60 - detik)
                  jam_sisa = str(sisa_jam)
                  menit_sisa = str(sisa_menit)
                  detik_sisax = int(sisa_detik%60)
                  detik_sisa = str(detik_sisax)
        elif menit < 55 :
             if detik == 0 :
                  sisa_menit = int(55 - menit)
                  sisa_detik = int(sisa_menit*60 - detik)
                  jam_sisa = str(sisa_jam)
                  menit_sisa = str(sisa_menit)
                  detik_sisax = int(sisa_detik%60)
                  detik_sisa = str(detik_sisax)
             else :
                  sisa_menit = int(54 - menit)
                  sisa_detik = int((sisa_menit +1)*60 - detik)
                  jam_sisa = str(sisa_jam)
                  menit_sisa = str(sisa_menit)
                  detik_sisax = int(sisa_detik%60)
                  detik_sisa = str(detik_sisax)
          
elif jam == 10 :
    if menit <5 :
        lebih_detik = int(detik//60)
        lebih_jam = 0
        lebih_menit = 0
        jam_lebih = str(lebih_jam)
        menit_lebih = str(lebih_menit)
        detik_lebih = str(lebih_detik)
    elif menit >=5 :
        lebih_jam = int(jam-10)
        lebih_menit = int( lebih_jam*60 + (menit - 5))
        lebih_detik = int( lebih_menit*60 + detik )
        detik_lebihx = int(lebih_detik%60)
        detik_lebih = str(detik_lebihx)
        jam_lebih = str(lebih_jam)
        menit_lebih = str(lebih_menit)
elif jam > 10 :
        lebih_jam = int(jam-10)
        lebih_menit = int( lebih_jam*60 + (menit - 5))
        menit_lebihx = int(lebih_menit%60)
        lebih_detik = int( lebih_menit*60 + detik )
        detik_lebihx = int(lebih_detik%60)
        detik_lebih = str(detik_lebihx)
        jam_lebih = str(lebih_jam)
        menit_lebih = str(menit_lebihx)
        

# perhitungan skor
b = int(25-a)
c = int(a*4 - b)
if jam == 9 and menit>55 :
     d = int(c+0)
elif jam == 10 and menit<5 :
     d = int(c+0)
elif jam <10 :
     d = int(c + (sisa_detik//(7*60+30))*2)
elif jam >= 10 :
     d = int(c- detik //(2*60+30))

if jam < 10 :
     print('owo memiliki sisa waktu sebesar {} jam {} menit {} detik'.format (jam_sisa, menit_sisa, detik_sisa))
     print(d)
elif jam >=10 :
     print('owo memiliki sisa waktu sebesar {} jam {} menit {} detik'.format(jam_lebih, menit_lebih, detik_lebih))
     print(d)

