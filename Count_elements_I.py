n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = []
d = []
for i in a:
    if i in b and i not in c:
        c.append(i)
for j in b:
    if j in a and i not in d:
        d.append(j)
print(len(c))

    