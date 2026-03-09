n = int(input())

p = list(map(int,input().split()))
orange = sum(p)
total = n*100


percent = (orange/total)*100
print(percent)
