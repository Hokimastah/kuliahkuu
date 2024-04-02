import math
a = int(input())
b = list(map(int, input().split()))
if len(b)> a :
    StopIteration
firsttime = input()
hari = ["Minggu" ,"Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]

e = (hari.index(firsttime) + math.lcm(*b)) % 7

print(hari[e])
