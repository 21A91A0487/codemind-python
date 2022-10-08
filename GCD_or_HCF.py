N,M=map(int,input().split())
def hcfnaive(a,b):
    if(b==0):
        return abs(a)
    else:
        return hcfnaive(b, a%b)
print(hcfnaive(N,M))
