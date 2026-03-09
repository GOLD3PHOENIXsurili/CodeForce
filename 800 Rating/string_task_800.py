s = input()

vowel = ["A","E","I","O","U","Y","a","e","i","o","u","y"]

new = ""

for i in range(len(s)):
    if s[i] not in vowel:
        new += s[i] 

s = "." + ".".join(map(str,new))
s = s.lower()
print(s)
