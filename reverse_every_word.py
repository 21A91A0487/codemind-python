n = input()
a = n.split()
b = [c[::-1] for c in a]
print(*b)