n=int(input())
s=0
r=n
n=n*n
while(n):
    k=n%10
    s=s+k
    n=n//10
if(r==s):
    print("Neon Number")
else:
    print("Not Neon Number")