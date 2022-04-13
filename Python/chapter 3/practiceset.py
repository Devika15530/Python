from datetime import date, datetime
from distutils.errors import LibError
from turtle import pen


name=input()
print("Good Morning",name)
Selecteddate=date.today()
letter='''Dear {},you are selected {}'''.format(name,Selecteddate)
print(letter)
str="Good  Morning  Devika"
print(str.find("  "))
str=str.replace("  "," ")
print(str)
letter="Dear Harry,\n \tThis Python course is nice \n.Thanks!"
print(letter)
