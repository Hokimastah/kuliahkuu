a, b = map(int,input().split())
arena = []
for i in range(a):
    x = input()
    y = [char for char in x]
    arena.append(y)

c = int(input())
d = input()
langkah = [char for char in d]
print(arena)
def jalan(arena,langkah,a,b):
    finish = 0
    step = 0
    for i in langkah:
        step+=1
        if i == "w":
            if a>=1 and a<=len(arena) and b>=0 and b<=len(arena[0]):
                if arena[a-1][b] == ".":
                    arena[a-1][b] = "#"
                    jalan(arena,langkah,a-1,b)
                elif arena[a-1][b] == "$":
                    arena[a-1][b] = "*"
                    finish = 1
                    return finish
                else : 
                    print(f"{step} Robot Menabrak Obstacle")
            else : 
                print(f"{step} Robot Menabrak Tembok")
                jalan(arena,langkah,a,b)
            
        elif i == "d":
            if a>=0 and a<=len(arena) and b>=0 and b<=(len(arena[0])-1):
                if arena[a][b+1] == ".":
                    arena[a][b+1] = "#"
                    jalan(arena,langkah,a,b+1)
                elif arena[a][b+1] == "$":
                    arena[a][b+1] = "*"
                    finish = 1
                    return finish
                else : 
                    print(f"{step} Robot Menabrak Obstacle")
            else : 
                print(f"{step} Robot Menabrak Tembok")
                jalan(arena,langkah,a,b)
                
        elif i == "a":
            if a>=0 and a<=len(arena) and b>=1 and b<=len(arena[0]):
                if arena[a][b-1] == ".":
                    arena[a][b-1] = "#"
                    jalan(arena,langkah,a,b-1)
                elif arena[a][b-1] == "$":
                    arena[a][b-1] = "*"
                    finish = 1
                    return finish
                else : 
                    print(f"{step} Robot Menabrak Obstacle")
            else : 
                print(f"{step} Robot Menabrak Tembok")
                jalan(arena,langkah,a,b)
        elif i == "s":
            if a>=0 and a<=(len(arena)-1) and b>=0 and b<=len(arena[0]):
                if arena[a+1][b] == ".":
                    arena[a+1][b] = "#"
                    jalan(arena,langkah,a+1,b)
                elif arena[a+1][b] == "$":
                    arena[a+1][b] = "*"
                    finish = 1
                    return finish
                else : 
                    print(f"{step} Robot Menabrak Obstacle")
            else : 
                print(f"{step} Robot Menabrak Tembok")
                jalan(arena,langkah,a,b)
    
        return finish

for i in range(a):
    for j in range(b):
        if arena[i][j] == "*":
            arena[i][j] = "#"
            jalan(arena, langkah, i, j)
            for k in arena:
                x = "".join(arena[k])
                print(x)
            if jalan(arena, langkah, i, j) == 1:
                print("Robot Mencapai Finish")
            else:
                print("Robot Tidak Mencapai Finish")