n=int(input())
c=0
a=list(map(int,input().split()))
for i in a:
    d=str(i)
    e=len(d)
    if e%2==0:
        c+=1
print(c)
    