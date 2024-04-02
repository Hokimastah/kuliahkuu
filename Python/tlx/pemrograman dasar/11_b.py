a, b = map(str,input().split())
while b in a:
    a = a.replace(b,"")
    
print(a)