with open("Devika.txt","w") as fo:
    fo.write("Files using with keyword")
    l=["this \n","is \n","an \n","example \n","for \n","writable \n","method \n"]
    lines=fo.writelines(l)#writes a list of strings
    #fo.readlines() gives u error because the file is open in write mode
