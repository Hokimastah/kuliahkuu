x = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a = input()
a = [char for char in a]
b = int(input())

ax = []
for i in a:
    ax.append(x[(x.index(i)+b)%26])
ax = "".join(ax)
print(ax)