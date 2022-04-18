from dataclasses import replace


fo=open("Donkey.txt","r")
date=fo.read()
fo.close()

fo=open("Donkey.txt","w")
fo.write(date.replace("donkey","######"))
fo.close()

fo=open("Donkey.txt","r")
print(fo.read())
print(fo.readlines())


