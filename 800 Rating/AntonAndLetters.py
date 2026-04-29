s = input()

unique = set()

for ch in s:
    if ch.isalpha():
        unique.add(ch)

print(len(unique))
