# n = int(input())

# total = 0

# for i in range(1,n+1):
#     new = ((-1)**i)*i

#     total = total + new

# print(total)

n = int(input())

if n%2 == 0:
    total = n//2
else:
    total = -(n+1)//2
print(total)

