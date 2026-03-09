# n = int(input())

# arr = []

# for i in range(n):
#     arr.append(input())

# group = 1

# for j in range(1,n):
#     if arr[j] != arr[j-1]:
#         group += 1
        
# print(group)




# new Approach

# Start
#  ↓
# Read first magnet
#  ↓
# group = 1
#  ↓
# Read next magnet
#  ↓
# Is it different from previous?
#         │
#    YES  │  NO
#    ↓    │
# group++ │
#         │
# Update previous magnet
#  ↓
# Repeat

n = int(input())

prev = input()
group = 1

for _ in range(n-1):
    curr = input()
    if curr != prev:
        group += 1
    prev = curr

print(group)
