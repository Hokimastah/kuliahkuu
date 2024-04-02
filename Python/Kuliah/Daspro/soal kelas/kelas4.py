def paternA(baris, kolom) :
    for b in range(baris):
        if (b%2==1):
            print(" ")
        for k in range(kolom):
            if (k%2==1):
                print('.')
            else :
                print('-')


def paternB(baris, kolom):
    for b in range(baris):
        if (b%2==0):
            print(" ")
        for k in range(kolom):
            if (k%2==1):
                print('-')
            else:
                print('.')

testcase = int(input())
for t in range(testcase):
    list_input = input().split()

    pola= list_input[0]
    baris = int(list_input[1])
    kolom = int(list_input[2])

    if(list_input == "A"):
        paternA(baris,kolom)
    else:
        paternB(baris,kolom)