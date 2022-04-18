fo=open("Devika.txt","w")
print(fo.tell())#tells the location of file pointer
print(fo.seek(10))#we can change the position of file pointer
print(fo.tell())
fo.close()
