import math
def isprime(num):
    sq = int(math.sqrt(num))
    for i in range(2,sq+1):
        if num%i == 0:
            return False
    else:
        return True

n = int(input())
if isprime(n):
    rev = 0
    while n:
        d = n%10
        n = n//10
        rev = rev*10+d
    if isprime(rev) == False:
        print("prime but not a circular prime")
    else:
        print("circular prime")
else:
    print("not prime")