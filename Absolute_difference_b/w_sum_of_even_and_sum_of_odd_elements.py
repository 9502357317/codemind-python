n=int(input())
s=0
p=0
a=list(map(int,input().split()))
for i in a:
    if i%2==0:
        s=s+i
    else:
        p=p+i
print(abs(p-s))