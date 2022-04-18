
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if((a>b)& (a>c) &(a>d)):
    print("%d is greater"%(a))
elif((b>a)&(b>c)&(b>d)):
    print("%d is greater"%(b))
elif((c>a)&(c>d)&(c>b)):
    print("%d is great"%(c))
else:
    print("%d is great"%(d))
