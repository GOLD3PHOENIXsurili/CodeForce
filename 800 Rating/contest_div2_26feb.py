# # Question A

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     p = list(map(int,input().split()))

#     hi = 0
#     ugly = -1

#     for i in range(n):
#         hi = max(hi,p[i])
#         if hi == i+1:
#             ugly = i
#             break
    
#     hi = 0
#     uglyc = 0
#     for i in range(n):
#         hi = max(hi,p[i])
#         if hi == i+1:
#             uglyc += 1

#     if uglyc > 1:
#         pos = p.index(n)

#         if pos > ugly:
#             p[ugly],p[pos] = p[pos],p[ugly]

#     print(*p)





t = int(input())

for _ in range(t):
    n = int(input())
    temp = n
    k = 1

    i = 2
    while i * i <= temp:
        if temp % i == 0:
            k *= i
            while temp % i == 0:
                temp //= i
        i += 1

    if temp > 1:
        k *= temp

    print(k)
    
    

     


print(i)