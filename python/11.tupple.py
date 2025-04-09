#tupple is an immuatable data types in python

a=(1,2,5,6)
print(type(a)) #<class tupple>

b=(1,)
print(type(b))  #<class tupple>


#tupple methode
#tupplename.count()
name=("rohan","priya","shruti","kiya")
print(name.count("rohan"))   #1

#tupple.Index
print(name.index("shruti"))  #2

#repeated
print(name*3)  

#membership:you can check if an item is exist in a tupple using the 'in' keyword
print("rohan" in name)  #it will return true

