s = input()
v = 'aeiou'
c=0
a=[]
for i in s:
    if i not in a:
        a.append(i)
for i in a:
    if i in v:
        c += 1
if(c==5):
    print(True)
else:
    print(False)