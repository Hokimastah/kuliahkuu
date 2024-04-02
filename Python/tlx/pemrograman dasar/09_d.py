x = list(map(int,input().split()))
a = x[0]
b = x[1]
matrix = []
for i in range(a):
    x = list(map(int,input().split()))
    matrix.append(x)

matrix2 = []
for i in range(b):
    x = []
    for j in range(a):
        x.append(str(matrix[a-j-1][i]))
    matrix2.append(x)

for i in matrix2:
    n = " ".join(i)
    print(n)