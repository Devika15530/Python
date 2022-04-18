#number which is divisible by itself and 1 is called prime number

n=int(input())
count=0
for i in range(2,10):
    print("%d"%count)
    if(n%i==0):

        count+=1
if(count<2):
    print(n ,"is prime")
