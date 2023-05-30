n=int(input())
s=0
a=list(map(int,input().split()))
for i in a:
    s=s+i
c=s/len(a)    
print("%.2f"%c)