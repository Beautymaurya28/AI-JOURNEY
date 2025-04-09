#set is a collction of well defined elements
s=set()
s.add(1)
s.add(2)
print(s)


#empty dictionary
b={}
print(b)

#empty set
d=set()  #don't use s={} as it will create an empty dictionay
print(type(d))


#value doesnot repeat in set
e={1,2,3,5,3,5,4,6,6,7,7}
print(e)

#sets methode
#1.add=this is most important methode in sets
box={1,2,"beauty",89.3,"tadad"}
box.add("hello")
print(box)


#3.copy
new_box=box.copy()
print(new_box)


#2.clear
box.clear() #it will remove all the element in set 
print(box)


#3.difference
set1={1,2,3,4,6,9}
set2={3,2,4,8,9,10}
print(set1.difference(set2))

#.difference_updates
#5.discard
set1.discard(3)
print(set1)

#6.intersection
set1={1,2,3,4,5,6}
set2={3,2,4,5,6,7,8,9}
print(set1.intersection(set2)) #return a new set with element common 

#operation on set
set={1,8,2,3}

#1.len(s)= return the legth of set.
print(len(set))

#2.setname.remove()=updates the set and remove gievn value from set
set.remove(2)
print(set)

#3.setname.pop
sets=set.pop()
print(sets)

#4.setname.clear
set.clear()
print(set)

#5.setname.Union
setss={1,2,3,4,8,11,23,34}
setss2={9,50}
unionsets=setss.union(setss2)
print(unionsets)

#5.setname.intersection
setss={1,2,3,4,8,11,23,34}
setss2={9,50,11,3,23}
intersectionsets=setss.intersection(setss2)
print(intersectionsets)