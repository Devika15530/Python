dict={}
for i in range(3):
    key=input("enter name")
    value=list(map(int,input().split()))#to get the list of integers as input
    d={key:value}
    dict.update(d)#adding values to dictionary
print(dict)
for key, value in dict.items():#to itterate through dictionary to sum each students marks
    if(((sum(value))/3)>40):
        x=((sum(value))/3)
        print("%s is pass by %d"%(key,x))
    else:
        x=((sum(value))/3)
        print("%s is fail by %d"%(key,x))


