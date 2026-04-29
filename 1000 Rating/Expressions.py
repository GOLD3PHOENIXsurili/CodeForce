a = int(input())
b = int(input())
c = int(input())

# print(max(
#     a + b + c,
#     a * b * c,
#     (a + b) * c,
#     a * (b + c),
#     a + (b * c),
#     (a * b) + c
# ))

print(max(a*b*c, (a+b)*c, a*(b+c), a+b+c))

# if any number of 1, adding is better
# if any number is >2 then multiplication gives the largest result