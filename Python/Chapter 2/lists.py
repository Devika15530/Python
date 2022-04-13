l=[10,20,30,40]
#print the elements from 0 to 3
a=l[0:3]
print(a)
#print the elements from 0 to 3 by default start index will 0
a=l[:3]
print(a)
#print the elements from 2 to end by default end of list
a=l[2:]
print(a)
#inserting the element
l[2]=25
print(l)
#2 lists
m=[[10,20,30],[40,50,60]]
print("1=",m[0][0],"2=",m[0][1],"3=",m[0][2])
print("1=",m[1][0],"2=",m[1][1],"3=",m[1][2])
#multidimensional lists
a=[[[10,20],[30,40]],[[50,60],[70,80]]]
print("1 is=",a[0][0][1],"2 is=",a[1][0][1]) 
#creating empty list
a=list()
a.append(1)
a.append([30,40])
#to insert so many elements at a time
a.extend([40,50,60,70])

#inserting element at position
a.insert(2,88)
print(a)
