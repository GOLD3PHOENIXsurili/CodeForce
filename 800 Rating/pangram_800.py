n = int(input())

s = input()

if n >= 26:
    s = s.lower()
    s = set(s)

    if len(s) >= 26:
        print("YES")
    else:
        print("NO")
else:
    print("NO")

    
    

