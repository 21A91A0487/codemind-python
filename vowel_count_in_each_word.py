s = input().split()
v = 'aeiouAEIOU'
c = 0
for i in s:
    c=0
    for j in i:
        if j in v:
            c += 1
    print(c,end=' ')