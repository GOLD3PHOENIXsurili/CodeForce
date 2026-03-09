borze = input()

ans = []

i = 0
while i < len(borze):
    if borze[i] == '.':
        ans.append("0")
        i += 1
    else:
        if borze[i + 1] == '.':
            ans.append("1")
            i += 2
        else:
            ans.append("2")
            i += 2

print("".join(ans))
