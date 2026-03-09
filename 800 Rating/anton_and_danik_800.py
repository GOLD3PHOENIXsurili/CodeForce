# n = int(input())

# s = input()

# countA = 0
# countB = 0
# for i in range(len(s)):
#     if s[i] == "A":
#         countA += 1
#     else:
#         countB += 1

# if countA > countB:
#     print("Anton")
# elif countA < countB:
#     print("Danik")
# else:
#     print("Friendship")

n = int(input())
s = input().strip()

countA = s.count("A")
countB = n - countA

if countA > countB:
    print("Anton")
elif countA < countB:
    print("Danik")
else:
    print("Friendship")
