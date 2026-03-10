coin = int(input())
value = list(map(int,input().split()))

total = sum(value)

mysum = 0
count = 0

new_value = sorted(value, reverse=True)

for i in new_value:
    mysum += i
    count += 1
    
    remaining = total - mysum

    if mysum > remaining:
        break

print(count)

