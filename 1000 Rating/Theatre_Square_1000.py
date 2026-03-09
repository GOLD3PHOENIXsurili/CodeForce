n,m,a = map(int,input().split())

if n% a == 0:
    tiles_length = n // a
else:
    tiles_length = (n // a) + 1
if m% a == 0:
    tiles_breadth = m // a  
else:
    tiles_breadth = (m // a) + 1


result = tiles_length * tiles_breadth

print(result)
