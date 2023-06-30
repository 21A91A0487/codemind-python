n = int(input())
s = str(n**2)
r = str(n)[::-1]
rev = str(int(r)**2)
if s[::-1] == rev:
    print(True)
else:
    print(False)