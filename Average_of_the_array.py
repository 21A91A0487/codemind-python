n = int(input())
l = list(map(int,input().split()))
s = 0
for i in range(0,len(l)):
    s += l[i]
avg = s/len(l)
print("{:.2f}".format(avg))