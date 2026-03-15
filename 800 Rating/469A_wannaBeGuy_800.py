n = int(input())

x = list(map(int,input().split()))
y = list(map(int,input().split()))

z = x + y

z = set(z)

if len(z) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")





