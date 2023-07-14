n = input()
b = n.split()
a = 'aeiouAEIOU'
l = []
for i in b:
    if i[0] in a and i[-1] not in a:
        l.append(i)
print(len(l))
        