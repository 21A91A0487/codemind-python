n,m = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(n)]
a = []
for i in range(1,n-1):
    for j in range(1,m-1):
        a.append(mat[i][j])
print(sum(a))