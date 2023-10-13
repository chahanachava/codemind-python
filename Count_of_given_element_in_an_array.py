a=int(input())
b=list(map(int,input().split()))
s=int(input())
c=0
for i in range(0,len(b)):
    if(b[i]==s):
        c=c+1
print(c)