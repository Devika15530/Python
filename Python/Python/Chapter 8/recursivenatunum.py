 #sum=((n*(n+1))/2)
def naturalnumber(number):
    sum=0
    if(number<=1):
        return number
    else:
        return number+naturalnumber(number-1)
c=naturalnumber(15)
print(int(c))

