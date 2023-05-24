n=int(input())
a=n*n
s=0
p=0
while n!=0:
    r=n%10
    n//=10
    s=s*10+r
q=s*s
while q!=0:
    c=q%10
    q//=10
    p=p*10+c
if a==p:
    print(True)
else:
    print(False)
