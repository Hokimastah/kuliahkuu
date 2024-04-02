s1 = input()
s2 = input()
s3 = input()
s4 = input()

x = s1
x = x.replace(s2,"")
idx = x.index(s3)+len(s3)
print(x[:idx]+s4+x[idx:])