n=int(input())
a=list(map(int,input().split()))
s=0
p=0
for i in range(0,n):
    if i%2==0:
        s=s+a[i]
    else:
        p=p+a[i]
if s-p==0:
    print("YES")
else:
    print("NO")