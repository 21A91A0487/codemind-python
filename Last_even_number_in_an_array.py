n = int(input())
l = list(map(int,input().split()))
b = 0
for i in l:
    if i%2 == 0:
        b = i
print(b)