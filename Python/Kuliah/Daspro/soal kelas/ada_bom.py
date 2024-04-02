a, b = map(int,input().split())
matrix = []
for i in range(a):
    x = input()
    y = []
    for char in x:
        y.append(char)
    matrix.append(y)

c = 0
for i in range(a):
    for j in range(b):
        if matrix[i][j] == 'x':
            
            if i-1 >= 0 and j-1 >= 0 and matrix[i-1][j-1] == '0':
                c+=1
            if i-1 >= 0 and matrix[i-1][j] == '0':
                c+=1
            if i-1 >= 0 and j+1 <= b-1 and matrix[i-1][j+1] == '0':
                c+=1
            if j-1 >= 0 and matrix[i][j-1] == '0':
                c+=1
            if j+1 <= b-1 and matrix[i][j+1] == '0':
                c+=1
            if i+1 <= a-1 and j-1 >= b-1 and matrix[i+1][j-1] == '0':
                c+=1
            if i+1 <= a-1 and matrix[i+1][j] == '0':
                c+=1
            if i+1 <= a-1 and j+1 <= b-1 and matrix[i+1][j+1] == '0':
                c+=1

print(c)