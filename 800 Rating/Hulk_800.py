n = int(input())

for i in range(1,n+1):
    if i%2 == 1:
        print("I hate ", end ="")

        if i == n:
            print("it",end ="")
        else:
            print("that ",end ="")

    elif i%2 == 0:
        print("I love ",end ="")

        if i == n:
            print("it",end ="")
        else:
            print("that ",end ="")




    