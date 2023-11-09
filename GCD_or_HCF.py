a,b=map(int,input().split())
k=min(a,b)
while 1:
    if a%k==0 and b%k==0:
        break
    else:
        k=k-1
print(k)