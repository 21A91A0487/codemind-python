n = int(input())
l = list(map(int,input().split()))
a = []
c = 0
for i in l:
    c += 1
    a.append(len(str(i)))
print(a.count(max(a)))