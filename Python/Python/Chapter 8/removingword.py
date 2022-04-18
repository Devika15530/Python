listofnames=list(input().split())
print(listofnames)
def removeword(word,listofnames):
    if(word in listofnames):
         listofnames.remove(word)
         return listofnames
    else:
        return "No such word found"
res=removeword("mai",listofnames)
print(res)

