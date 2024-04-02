a = int(input())

if a <= 40 :
    b = 'E'
elif a <= 55 :
    b = 'D'
elif a <= 60 :
    b = 'C'
elif a <= 65 :
    b = 'BC'
elif a <= 75 :
    b = 'B'
elif a <= 85 :
    b = 'AB'
else :
    b = 'A'

print(b)