n = int(input())
sumV = 0
for i in range(1,n):
    if(n%i==0):
        sumV = sumV+i
if(sumV==n):
    print("True")
else:
    print("False")