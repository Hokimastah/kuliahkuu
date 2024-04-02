a = int(input())
biner = ""
def bit(x,biner):
    if x == 1:
        biner = biner + "1"
        biner = [char for char in biner]
        biner.reverse()
        return int("".join(biner))
    elif x % 2 == 1:
        x//=2
        biner = biner + "1"
        return bit(x,biner)
    else:
        x//=2
        biner = biner + "0"
        return bit(x,biner)
print(bit(a,biner))