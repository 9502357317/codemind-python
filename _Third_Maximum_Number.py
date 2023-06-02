n=int(input())
a=list(map(int,input().split()))
d=set(a)
e=sorted(d)
if n>=3:
    print(e[-3])
else:
    print(max(e))