n = int(input())
l = list(map(int,input().split()))
a = []
for i in range(n):
    if l[i] != 0:
        a.append(i)
print(a[-1])