m,n = map(int,input().split())
X = m * n
result = 0
if X%2 == 0:
    result =  X // 2
else:
    result = (X // 2)

print(result)
