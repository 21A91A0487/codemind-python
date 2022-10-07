n=int(input())
sqr=n*n
sumofdigit=0
while sqr>0:
    sumofdigit=sumofdigit+sqr%10
    sqr=sqr//10
if(n==sumofdigit):
    print("Neon Number")
else:
    print("Not Neon Number")