

n=int(input())
s=0
a=list(map(int,input().split()))
for i in range(0,n):
    if i%2==0:
        s=s+a[i]
print(s)






