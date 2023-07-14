n = input()
a = ' '
l = []
for i in n:
    if i not in a:
        l.append(i)
print(len(l))