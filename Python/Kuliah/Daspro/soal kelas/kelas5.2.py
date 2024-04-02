a = int(input())
if a == 1:
    print('*')
else:
    print('*')
    for i in range(2,a+1):
    
        print('*'*i)
        print('*')
        print('*'*(a-(i-1)))