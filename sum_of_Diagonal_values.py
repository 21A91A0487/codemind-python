n,m = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(n)]
a = []
for i in range(n):
    b = 0
    for j in range(m):
        if i == j or i+j == n-1:
            b += mat[i][j]
    a.append(b)
print(sum(a))