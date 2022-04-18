

a=input().split()#to read list of values
print(type(a))
b=10
#program to check whether given number is present in list or not
#IN is a membership operator
#indendation is mandatory in python use semicolon it will automatically create indendation
if(b in a):
    print("%d exists in a "%(b))
else:
    print("%d not exists in a"%(b))
print("Hello","Welcome","to","python")
#sep is used to place sepeartor between strings
print("Hello","Welcome","to","python",sep="-")
#format specifiers
print("%d is int %f is float"%(10,20))