n = int(input())
l = list(map(int,input().split()))
n,m = map(int,input().split())
c = []
d = []
for i in l:
    if i<n or i>m:
        c.append(i)
    else:
        d.append(i)
if not c:
    print(-1)
else:
    print(*c)