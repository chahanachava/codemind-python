n=int(input())
a=0
b=1
while a<=n:
    c=a+b
    if a==n:
        print("True")
        break
    a=b
    b=c
else:
    print("False")