for t in range(int(input())):
    n = int(input())
    l = [int(k) for k in input().split()]
    odd = 0
    for i in range(len(l)):
        if l[i]%2 == 0:
            pass
        else:
            odd += 1
    if odd%2 == 0:
        print(int(odd/2))
    else:
        print(int(odd//2))
