lst = list(map(int,input().split()))

n = len(lst)

s = set(lst)
m = len(s)

result = n - m

print(result)

