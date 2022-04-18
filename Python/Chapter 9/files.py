#Three main steps while working with file open,read/write/append,close
#If file dosen't exists in write and append mode it will create one for u
#In read if file dosen't exists  it willl give u error
fo=open("Devika.txt","w")
fo.write("Hey")
fo.write("Devika")
fo.close()

