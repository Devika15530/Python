from operator import indexOf
from tkinter import TRUE


a=[10,20,30,40]
a*=3
print(a.count(20))
a.pop()#removes last element
print(a.index(30))
a.insert(0,99)
print(a)
a.reverse()
print(a)
a.sort()#sorting in ascending order
print(a)
a.sort(reverse=TRUE)#sorting in descending order
print(a)
print(a.index(20))#first occuring index
########List comprehnsion##########
a=[ele for ele in range(10)]#element itteration
print(a)
a=[ele*2 for ele in range(10)]#square the element
print(a)
a=[ele for ele in range(10) if(ele%2==0)]#only insert if the condition satisfies
print(a)