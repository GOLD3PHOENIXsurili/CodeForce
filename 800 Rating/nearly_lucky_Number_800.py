# #if the number of lucky digits in it is a lucky number
n = int(input())
def valid(n):
    count = 0
    while n>0:
        if n%10 == 7 or n%10 == 4:
            n = n//10
            count += 1
            continue
        n = n//10
    return count

pox = valid(n) 


result = pox>0
while pox>0:
    digit = pox %10
    if digit%10 != 7 and digit%10 != 4:
        result = False
        break
    pox = pox//10

if result:
    print("YES")
else:
    print("NO")









# THIS CODE BRLOW IS CORRECT

# n = input().strip()
# count = 0
# for i in range(len(n)):
#     if n[i] == "4" or n[i] == "7":
#         count += 1

# update = str(count)

# result = count > 0
# for j in range(len(update)):
#     if update[j] != "4" and update[j] != "7":
#         result = False
#         break

# if result:
#     print("YES")
# else:
#     print("NO")

