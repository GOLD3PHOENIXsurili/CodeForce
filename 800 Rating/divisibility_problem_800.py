n = int(input())

ans = []
for i in range(n):
    a,b = map(int,input().split())

    if a% b == 0:
        ans.append(0)
    else:
        ans.append(b - (a%b))
    
for x in ans:
    print(x)

    