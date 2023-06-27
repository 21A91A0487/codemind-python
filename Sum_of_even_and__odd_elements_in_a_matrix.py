n,m = map(int,input().split())
mat = []
a = []
b = []
for i in range(n):
    lst = list(map(int,input().split()))
    mat.append(lst)
for i in mat:
    for j in i:
        if j%2 == 0:
            a.append(j)
        else:
            b.append(j)
print(sum(a),sum(b))