n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = []
for i in range(n):
    c.append(int(a[i]+int(b[i])))
print(*c)