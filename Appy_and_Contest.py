import math
t=int(input())
for k in range(t):
    n,a,b,k=map(int,input().split())
    p=n//a
    q=n//b
    c=math.gcd(a,b)
    d=(a*b)//c
    s=n//d
    if((p+q-2*s)>=k):
        print('Win')
    else:
        print('Lose')