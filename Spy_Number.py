n=int(input())
s=0
s1=1
while(n!=0):
    r=n%10
    n=n//10
    s=s+r
    s1=s1*r
if(s==s1):
    print("Spy Number")
else:
    print("Not Spy Number")