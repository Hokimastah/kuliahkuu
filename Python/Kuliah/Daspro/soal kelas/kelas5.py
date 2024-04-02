def gunung(x): 
    if x == 1 :
        print('*')
        return 
    else :
        gunung(x-1)
        print('*' * x)
        gunung(x-1)

a = int(input())
gunung(a)