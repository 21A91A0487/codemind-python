s = input()
v = 'AEIOUaeiou'
c=0
a=[]
for i in s:
    if i not in a:
        a.append(i)
for i in a:
    if i in v:
        print(i,end=' ')
        c+=1
if(c==0):
    print(-1)
    