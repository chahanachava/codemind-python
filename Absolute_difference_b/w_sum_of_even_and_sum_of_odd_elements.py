n=int(input())
x=list(map(int,input().split()))
s=0
s1=0
for i in range(0,len(x)):
    if x[i]%2==0:
        s=s+x[i]
    else:
        s1=s1+x[i]
print(abs(s-s1))