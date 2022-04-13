#creating empty set
s=set()
#s={} create dictionary
s={10,20,30,40}#unordered
s.add(50)
s.discard(30)
#s.remove(100) error
s.pop()
print(len(s))
print(10 in s)
for ele in s:
    print(ele)
#s[0] assignment is not possible
print(s)

s={10,20,30,40,50}
t={10,20,30,40,80,90,70}
print(s.issubset(t))#all elements in s must be present in t 50 is not present so it will retunr false
print(s.issuperset(t))
print(s.union(t))
print(s.intersection(t))
print(s.difference(t))#different elements only present in set1
print(t.difference(s))
print(s.symmetric_difference(t))
s.difference_update(t)#above all new sets will create but for this set1 will updatew
print(s)
s=t.copy()#copies elements
print(s)

#s.add([3,4,5])#TypeError: unhashable type: 'list'
s.add((3,4,5))#can add tuples to sets 
s.add({4:5})
print(s)