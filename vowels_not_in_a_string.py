s = input()
v = 'aeiou'
c=0
a=[]
for i in v:
    if i not in s:
        a.append(i)
for i in a:
    if i in v:
        print(i,end=' ')
        c+=1
if(c==0):
    print(0)
    