n = int(input())
a = list(map(int,input().split()))

mx = max(a)
mn = min(a)

lidx = a.index(mx)
ridx = len(a) - 1 - a[::-1].index(mn)

moves = lidx + (n-1-ridx)

if lidx > ridx:
    moves -= 1

print(moves)