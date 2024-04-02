def gunung(x):
    if x>0:
        gunung(x-2)
        print('*' * x)
        gunung(x-2)

a = int(input())
gunung(a)