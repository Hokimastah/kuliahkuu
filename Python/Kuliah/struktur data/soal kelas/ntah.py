stack = input()
hasil = []
hasil2 = []
for i in stack:
    if i == "(" or i == "{" or i == "[" :
        hasil.append(i)
    else :
        if i == ")":
            if hasil[-1] == "(":
                hasil2.append(hasil[-1])
                hasil.pop()
                hasil2.append(i)
            else : 
                print("salah")
                break
        elif i == "}":
            if hasil[-1] == "{":
                hasil2.append(hasil[-1])
                hasil.pop()
                hasil2.append(i)
            else : 
                print("salah")
                break
        elif i == "]":
            if hasil[-1] == "[":
                hasil2.append(hasil[-1])
                hasil.pop()
                hasil2.append(i)
            else : 
                print("salah")
                break

hasil2 = "".join(hasil2)
print(hasil2)