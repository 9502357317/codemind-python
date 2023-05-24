n=int(input())
m=n
s=0
while m!=0:
    r=m%10
    m//=10
    s=s*10+r
if s==n:
    print(True)
else:
    print(False)