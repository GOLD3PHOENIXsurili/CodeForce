given = input()

new = given.split("+")
new.sort()
result = "+".join(map(str,new))
print(result)