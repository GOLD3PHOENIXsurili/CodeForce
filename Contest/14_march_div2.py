# Candy

# t = int(input())

# for _ in range(t):

#     m = int(input())

#     rep = {}

#     for j in range(m):
#         row = list(map(int, input().split()))

#         for x in row:
#             rep[x] = rep.get(x,0) + 1

#     mx = max(rep.values())

#     if mx > m*(m-1):
#         print("NO")
#     else:
#         print("YES")



# stamina and task
t = int(input())

for _ in range(t):

    n = int(input())

    c = []
    p = []

    for _ in range(n):
        ci, pi = map(int, input().split())
        c.append(ci)
        p.append(pi)

    dp = 0

    for i in range(n-1, -1, -1):

        prob = 1 - p[i]/100

        dp = max(dp, c[i] + prob * dp)

    print(dp)