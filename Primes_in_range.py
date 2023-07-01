n = int(input())
m = int(input())
l = []
for num in range(n,m+1):
    if num > 1:
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                break
        else:
            l.append(num)
print(len(l))