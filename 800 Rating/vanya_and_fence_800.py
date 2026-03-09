n,t = map(int,input().split())

x = list(map(int,input().split()))
count = 0
for i in x:
    if i <= t:
        count += 1
    else:
        count += 2


# count = sum(1 if i <= t else 2 for i in x)    optimised


print(count)
