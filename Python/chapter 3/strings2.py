#isalnum() checks for alphabets or numbers
s="abc123"
print(s.isalnum())#true
s="abc"
print(s.isalnum())#true
s="123"
print(s.isalnum())#true
s="abc@123"
print(s.isalnum())#false
#isalpha checks for alphabets isdigit checks for numbers
s="abc"
s1="123"
print(s.isdigit())#false
print(s.isalpha())#true
print(s1.isalpha())#false
print(s1.isdigit())#true
#isspace
s=" "
s1="dev"
print(s.isspace())#true
print(s1.isspace())#false
s="abcd"
s1="ABCD"
s2="abCD"
print(s.isupper())#false
print(s1.isupper())#true
print(s2.isupper())#false
print(s.islower())#true
print(s1.islower())#false
print(s2.islower())#false
s="Welcome to python"
s1="Welcome To Python"
print(s.istitle())#False because every word first char must be capital
print(s1.istitle())#true
s="Python"
print(s.ljust(10,"*"))#Python****
print(s.rjust(10,"-"))#----Python
print(s.upper())
s="    Python"
print(s.strip())
print(s.lstrip())
print(s.rstrip())