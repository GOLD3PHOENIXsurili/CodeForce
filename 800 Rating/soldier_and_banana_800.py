k,n,w = map(int,input().split())

sum = w*(w+1)//2

price = sum *k

# if he already has enough, then he doesn't need to borrow
borrow = max(0,price - n)
print(borrow)