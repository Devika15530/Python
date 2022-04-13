import math
import random
print(math.ceil(10.5))#upper value
print(math.floor(10.5))#lower value
print(math.factorial(5))
l=[10,20,30,40]
print(math.fsum(l))#sum the list of elements
print(math.isqrt(5))
print(math.pow(2,3))

r=[10,20,30,40]
print(random.shuffle(r))
print(random.choice(r))#print random number from list
print(random.choices(r,k=2))#print 2 random numbers from list
print(random.randrange(10,15,1))#print random number between 10-15
print(random.random())

print(random.uniform(10,15))