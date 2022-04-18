#Read 8 numbers and print only unique values
numbers=set()#creating empty set beacuse it will store only unique values
for i in range(8):
  value=int(input())#reading values from user
  numbers.add(value)#adding values to set
print(numbers)#printing set


#can we have a set with 8(int) and "8"(str)
dup=set()
dup.add(8)
dup.add("8")
print(dup)#yes we can have 

#length of the set
s=set()
s.add(10)
s.add(10.0)
s.add("10")
print(len(s))###2
#print(s[0])TypeError: 'set' object is not subscriptable


#cannont use list inside set and also dict we cannot use tuple we can use
#s={8,7,12,{"dev",[12,3,4]}}
