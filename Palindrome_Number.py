n=int(input())
for i in range(1,n+1):
    a=int(input())
    m=a
    s=0
    while m!=0:
        r=m%10
        m//=10
        s=s*10+r
    if a==s:
        print(True)
    else:
        print(False)
    