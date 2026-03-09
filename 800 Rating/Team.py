# n = int(input())

# anns = 0
# for i in range(n):
#     given = input().split()
    
#     count = 0
#     for j in range(3):
#         if given[j] == '1':
#             count += 1
#     if count > 1:
#         anns += 1
# print(anns)

        

n = int (input())

count = 0
for i in range(n):
    row = list(map(int,input().split()))

    if sum(row) > 1:
        count += 1
print(count)
