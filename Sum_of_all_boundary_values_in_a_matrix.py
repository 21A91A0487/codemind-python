n,m = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(n)]
s = 0
for i in range(1,n-1):
    for j in range(1,m-1):
        mat[i][j] = 0
for i in mat:
    for j in i:
        s += j
print(s)