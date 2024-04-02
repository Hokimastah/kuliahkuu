t = int(input())

for i in range(t):
    n, m, s = input().split()
    n = int(n)
    m = int(m)
    if s == 'right' :
        pagar = '##'
    else : pagar = '#'

    if m%2 == 0 :
        dot = '..'
    else : dot = '.'
    paket = pagar + dot + pagar
    
    for j in range(n):
        if s == 'right' :
            print(" "*j + paket)
        else : print(" "*(n-j) + paket)

