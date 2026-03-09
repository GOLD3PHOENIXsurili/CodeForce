# n,p = map(int,input().split())

# lst = []
# for i in range(1,n+1):
#     if i % 2 != 0:
#         lst.append(i)
# for i in range(1,n+1):
#     if i %2 == 0:
#         lst.append(i)


# print(lst[p-1])    # TLE


n,p = map(int,input().split())

odd = (n+1)//2

if p<= odd:
    print(2*p -1)
else:
    print(2*(p-odd))
    
