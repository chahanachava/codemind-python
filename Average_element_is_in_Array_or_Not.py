n=int(input())
num=list(map(int,input().split()))
s=sum(num)//n
print(s in num)