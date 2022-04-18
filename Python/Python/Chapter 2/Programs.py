#input() will take everything as a string need conversion
#program to print greater number among 3 numbers
a=int(input("Enter a value"))
b=int(input("Enter b value"))
c=int(input("Enter c value"))
print(type(a))
if(a>b):
    if(a>c):
        print("a is greater",a)
    else:
        print("b is greater",b)
else:
    if(b>c):
        print("b is greater",b)
    else:
        print("c is greater")

#greater from  2 numbers
if(a>b):
    print("a is greater")
elif (a<b):
    print("b is greater")
else:
    print("Both are equal")