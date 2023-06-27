n,m = map(int,input().split())
mat = []
for i in range(n):
    lst = list(map(int,input().split()))
    mat.append(lst)
se = 0
so = 0
for i in range(n):
    for j in range(m):
        if j %2 == 0:
            se += mat[i][j]
        else:
            so += mat[i][j]
print(se+so)