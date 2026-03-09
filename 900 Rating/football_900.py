n = input().strip()
count = 1
for i in range(1,len(n)):
    if n[i] == n[i-1]:
        count +=1 
        if count >= 7:
            print("YES")
            break
    else:
        count = 1
else:
    print("NO")

# n = input().strip()

# if "0000000" in n or "1111111" in n:
#     print("YES")
# else:
#     print("NO")

