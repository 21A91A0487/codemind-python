n,m = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(n)]
a = []
for j in range(m):
    lst = []
    for i in range(n):
        lst.append(mat[i][j])
    a.append(lst)
b = 0
for i in a:
    c = sorted(i)
    if i == c:
        b += 1
print(b)
        