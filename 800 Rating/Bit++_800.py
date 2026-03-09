n = int(input())
count = 0

for i in range(n):
    given = input()
    if given == "++X" or given == "X++":
        count += 1 
    elif given == "--X" or given == "X--":
        count -= 1
print(count)
