text=input()
if(text.__contains__("make a lot of money")|text.__contains__("buy now")|
text.__contains__("subscribe this")|text.__contains__("click this")):
    print("spam")
else:
    print("normal")


#without bulit in method and using memebership
text = input("Enter the text\n")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")