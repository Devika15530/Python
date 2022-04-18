#lambda function or anonymous functions without any name
add=lambda a,b:a+b
print(add(3,2))

#recursion
#base condition and recursive call

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(5))