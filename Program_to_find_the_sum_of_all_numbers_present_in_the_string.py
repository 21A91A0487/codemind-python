s = input()
a = 0
for i in s:
    if i >= '0' and i <= '9':
        a = a+ord(i) - 48
print(a)