n,m = map(int,input().split())
mat = []
a = []
for i in range(n):
    lst = list(map(int,input().split()))
    mat.append(lst)
for i in range(m):
    s = 0
    for j in range(n):
        s += mat[j][i]
    a.append(s)
print(*a)