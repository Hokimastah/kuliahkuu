N = int(input())
is_ganjil = 0
while (N>1) :   
    if (N%2)==1 :
        is_ganjil = 1
        break
    N/=2
if is_ganjil == 1 :
    print('bukan')
else:
    print('ya')