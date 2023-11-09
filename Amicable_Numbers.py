a=int(input())
b=int(input())
s1=0
s2=0
for i in range(1,max(a,b)):
    if a%i==0 and i!=a:
        s1=s1+i
    if b%i==0 and i!=b:
        s2=s2+i
if s1==b and s2==a:
    print("Amicable")
else:
    print("Not Amicable")
        