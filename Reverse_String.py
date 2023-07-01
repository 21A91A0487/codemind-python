n = input()
a = n.split()[::-1]
l = []
for i in a:
    l.append(i)
print(*l)