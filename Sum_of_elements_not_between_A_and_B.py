n = int(input())
l = list(map(int,input().split()))
n,m = map(int,input().split())
a = []
for i in l:
    if i<n or i>m:
        a.append(i)
print(sum(a))