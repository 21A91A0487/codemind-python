n = int(input())
l = list(map(int,input().split()))
a = []
for i in l:
    if i not in a and i%2 == 1:
        a.append(i)
print(len(a))