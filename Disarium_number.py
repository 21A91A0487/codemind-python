n = int(input())
a = str(n)
b = []
for i in a:
    b.append(int(i)**(a.index(i)+1))
    c = sum(b)
if n == c:
    print(True)
else:
    print(False)