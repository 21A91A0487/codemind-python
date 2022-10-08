def hcfnaive(a,b):
    if(b==0):
        return abs(a)
    else:
        return hcfnaive(b,a%b)
N,M=map(int,input().split())
print(hcfnaive(N,M))