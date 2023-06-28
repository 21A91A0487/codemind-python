n,m = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(n)]
s = 0
c = 0
for i in mat:
    c = sorted(i)
    if i == c or i == c[::-1]:
        s += 1
print(s)