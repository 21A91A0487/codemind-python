s = input()
c = 0
for i in s:
    if s.count(i) == 1:
        c += 1
if len(s) == c:
    print(True)
else:
    print(False)