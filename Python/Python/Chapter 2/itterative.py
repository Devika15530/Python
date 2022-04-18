n=int(input("enter n value"))
i=0
while(i<n):
    print(i)
    i+=1

#for loop
#can be exceuted in 2 types 1.sequence 2.Range
#Range(start,stop,step)-->start default-0,stop mandataory,step default 1 range(6)=range(0,6,1)
for i in range(0,6,1):
    print(i,end=" ")
#Both are same
for i in range(6):
    print(i,end=" ")
for i in range(0,6,2):
    print(i,end=" \n")#o/p 0 2 4
#like foreach in c#
str="Devika"
for letter in str:
    print(letter)
#nested for
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print(" ")
     

