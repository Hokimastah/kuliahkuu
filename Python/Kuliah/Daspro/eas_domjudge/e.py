a = int(input())
m_akhir= []
m2 = []
for i in range(a):
    n, m = map(int,input().split())
    m2.append(m)
    matrix = []
    for i in range(n):
        x = list(map(int,input().split()))
        matrix.append(x)
    m_akhir.append(matrix)

def muter(m,matrix):
    if m%4 == 1:
        matrix2 = []
        for i in range(len(matrix)):
            mboh = []
            for j in range(len(matrix)):
                mboh.append(matrix[j][len(matrix)-i-1])
            matrix2.append(mboh)
    elif m%4 == 2:
        matrix2 = []
        for i in range(len(matrix)):
            mboh = []
            for j in range(len(matrix)):
                mboh.append(matrix[len(matrix)-i-1][len(matrix)-j-1])
            matrix2.append(mboh)
    elif m%4 == 3:
        matrix2 = []
        for i in range(len(matrix)):
            mboh = []
            for j in range(len(matrix)):
                mboh.append(matrix[len(matrix)-j-1][i])
            matrix2.append(mboh)
    else: matrix2 = matrix
    return matrix2

for i in range(a):
    x = muter(m2[i],m_akhir[i])
    for j in x:
        mboh = " ".join(map(str,j))
        print(mboh)