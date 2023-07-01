import math
def isprime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    else:
        return True
n = int(input())
rev=str(n)[::-1]
if isprime(int(rev)) == False and isprime(n)==True:
    print("prime but not a circular prime")
elif isprime(n)==True and isprime(int(rev))==True:
    print('circular prime')
else:
    print('not prime')

        