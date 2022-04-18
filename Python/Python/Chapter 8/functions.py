#built in functions
#user defined functions
#function defintion and function call will be there
def add(a,b):#user defined functions will always start with def
    print(a+b)
add(10,30)

#no of parameters should match with function call and args
#default arguments
#they must be last 
def sum(a,b=40):
    print(a+b)
sum(20)#60
sum(10,10)#can be overided 20

#keyword argd
#no need to follow position
def display(a,b,c):
    print(a,b,c)
display(c=10,b=5,a=0)

#aribitary args
#only one parameter will accept miltiple values
def display(* marks):
    print(marks)#(10,20,30,40)
    print(marks[2])#30

display(10,20,30,40)

#global variable
#available to all over the program
#local varialble available till functionends
a=100
def display():
    print(a)
display()
#if both have same name local has first priority
def samenames():
    a=200
    print(a)#200
samenames()

def declaringglobalvar():
    global a
    a=a+1#if u dont declare global a it will show u error because it consider a as local  
    print(a)
declaringglobalvar()