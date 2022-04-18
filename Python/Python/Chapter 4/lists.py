#PROGRAM TO GET FRUITS LIST FROM USER AND DISPLAY IT
n=int(input("enter how many fruits u want to enter"))
Fruits=list()
for i in range(n):
    fruit=input("enter fruit name")
    Fruits.append(fruit)

print(Fruits)
#Sorting marks
Marks=list()
for i in range(6):
    marks=int(input())
    Marks.append(marks)
print(Marks)
Marks.sort()
print(Marks)

a=[10,20,30,40,50]
print(type(a[0]))
a=[ele+4 for ele in a]#adding 4 to each item by using list comprehension
print(a)
