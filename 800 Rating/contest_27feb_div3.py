# # PROBLEM A
# n = int(input())
# for i in range(n):
#     t = int(input())
#     x = list(map(int,input().split()))

#     max_value = max(x)
#     count = 0
    
#     for j in x:
#         if j == max_value:
#             count += 1 
#     print(count)


# t = int(input())

# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
    
#     max_value = max(a)
#     count = a.count(max_value)
    
#     print(count)



# PROBLEM B

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     x = list(map(int,input().split()))

#     is_sorted = True

#     for i in range(0,n-1):
#         if x[i] > x[i+1]:
#             is_sorted = False
#             break

#     if is_sorted:
#         print(n)
#     else:
#         print(1)



# PROBLEM C   STACK

t = int(input())
for _ in range(t):
    n = int(input())
    x = input()

    stack = []

    for ch in x:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)


    if not stack:
        print("YES")
    else:
        print("NO")
        

