fo=open("contains.txt","r")
data=fo.readlines()

for i in range(data.__len__()):
    if(data[i].__contains__("python")):
        print("yes")
        print("line number %d"%(i))
    
fo.close()