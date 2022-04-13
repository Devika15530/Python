str="Devika"
print(str[0])#D
print(str[-1])#a reverse indexing
print(str[1:4])#evi
print(str[:3])#dev by default starting index is 0
print(str[2:])#vika by default ending index is last
str="yours's"
print(str)
#str='your's' error code
str=''' hey
Welcom to python'''
print(str)
#Format method
print("{}is an integer and{} is float".format(10,10.5)) #10is an integer and10.5 is float
print("{1}is an integer and{0} is float".format(10.5,10))#10is an integer and10.5 is float
print("{2}is an integer and{3} is float".format(10.5,10,11,11.5))#11is an integer and11.5 is float
s="dev"
print(s*2)#devdev
print('d' in s)#true
print('D' in s)#false
print('de' in s)#true
print('dv' in s)#false
for letter in s:
    print(letter)
for i in range(len(s)):
    print(s[i])
#s[2]='z' error intializing is not possible
s="welcome to pyhton"
print(s.capitalize())#first letter will be captial
s="python"
print(s.center(10,'*'))#**python** python would be centered remaining will be filled with *
s="welcome to python programming"
print(s.count('o'))#total count of occurences of o
print(s.count('o',8,len(s)))#from 8 to last how many occurences of o
print(s.endswith("ing"))#true
print(s.startswith("python"))#False
print(s.find('o'))#4 first occurence
print(s.rfind('o'))#20 from last first occurence
print(s.index('o'))#4
#print(s.index('z')) error beacuse it is not there in string
print(s.find('z'))#-1
