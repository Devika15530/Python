friends={}
for i in range(4):
    name=input("enter your name:")
    favlang=input("enter favourite langaugae")
    frand={name:favlang}
    friends.update(frand)
friendname=input("enter friend name to know fav lang")
print(friends)
print(friends[friendname])

#if you enter the duplicate keys it will be automatically removed from dictionary
