n = int(input())
a = str(n**2)
b = str(n)[::-1]
rev = str(int(b)**2)
if a[::-1] == rev:
    print(True)
else:
    print(False)