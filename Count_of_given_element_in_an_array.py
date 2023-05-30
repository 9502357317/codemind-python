n=int(input())
a=list(map(int,input().split()))
b=int(input())
if b not in a:
    print('0')
else:
    print(a.count(b))