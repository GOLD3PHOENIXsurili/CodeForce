n = int(input())

curr = 0
max_cap = 0


for i in range(n):
    exit, enter = map(int,input().split())

    curr -= exit
    curr += enter

    max_cap = max(max_cap,curr)

    


print(max_cap)
