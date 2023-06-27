n,m = map(int,input().split())
mat = []
a = []
for i in range(n):
    lst = list(map(int,input().split()))
    mat.append(lst)
for i in mat:
    a.append(sum(i))
print(max(a))