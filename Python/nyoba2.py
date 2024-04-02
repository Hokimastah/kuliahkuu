a, b = map(int,input().split())
matrix = []

for i in range(a):
    y = input()
    z = [char for char in y]
    matrix.append(z)

        
def jalan(matrix, x, y, z):
    if matrix[y][z] == '.' and y<=len(matrix) and y >= 0 and z <= len(matrix[0]) and z >= 0 :
        matrix[y][z] = '#'
        if matrix[y][z] == '*':
            matrix[y][z] = '#'
            return
        if matrix[y-1][z] == '.' :
            x.append('W')
            jalan(matrix, x, y-1, z)
        elif matrix[y][z-1] == '.' :
            x.append('D')
            jalan(matrix, x, y, z-1)
        elif matrix[y][z+1] == '.' :
            x.append('A')
            jalan(matrix, x, y, z+1)
        elif matrix[y+1][z] == '.' :
            x.append('S')
            jalan(matrix, x, y+1, z)
        return

x = []
jalan(matrix, x, a, b)
print(x)
print(len(x))
print(matrix)
        
        
        