from os import name


dict={}
print(type(dict))
dict={"name":"Devika","phnno":"9912897822"}#Key Value Pair
print(dict["name"])
dict['college']='KHIT'
d1={"branch":"CSE"}
dict.update(d1)
print(len(dict))
print(dict)
#############dict comprhension############
d={i:i**2 for i  in range(10)}
print(d)
d={i:i+1 for i in range(10) if i%2==0}
print(d)
dict={"name":{"fname":"Python","name":"Programming"},"Duration":5}
print(dict['name'])
print(dict['name']['fname'])
s=dict.copy()#copy elements
print(s)
d={"a":3,"b":4,"c":5}
print(d.items())#dict_items([('a', 3), ('b', 4), ('c', 5)])
print(d.values())
print(d.keys())
d={"marks":[1,2,3,4]}#can declare list a values
dict={
     "anotherdict":{"haarry","Player"}
     }
print(d)
print(dict['anotherdict'])

#can access by using 
print(d.get('marks'))
print(d["marks"])
#both will give the same o/p when the key is present in dictionary
#when key is not present get will return none and next one will give error
print(d.get('class'))
print(d['class'])