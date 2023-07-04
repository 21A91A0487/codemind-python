n = int(input())
l = list(map(int,input().split()))
n,m = map(int,input().split())
a = []
b=[]
for i in l:
    if i<n or i>m:
        a.append(i)
    else:
        b.append(i)
if len(a)==0:
    print(-1)
else:
    print(max(a))