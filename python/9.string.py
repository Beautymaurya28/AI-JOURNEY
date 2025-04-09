
#intro of string
a='beauty' #single qoutes string
a1="beauty"  #double qoutes string
a2="""beauty"""  #tripple qoutes string
print(a,a1,a2)


#how to find length of any string
nameshort=len(a2)
print(nameshort)
nameshort=a2[0:3]
print(nameshort)
character1=a2[1]
print(character1)
negative_indix=a1[-3:-1]
print(negative_indix)

#negative slicing
name="mourya"
print(name[-4:-1])
print(name[2:5])

word="amazing"
print(word[1:6:3])
print(word[0:])
print(word[:6])

#string function
#1.length() function
a="beauty"
length=len(a)
print(length)

#2.string-endswith
print(a.endswith("ter"))  #it will give the false
name="beauty"
print(name.endswith("ty"))
#3.string-startswith
print(a.startswith("bea"))  #it will  give the true
#4.string.count("c")
string="abdkgjdfjigdjkld"
count=string.count("c")
print(count)

mystring="beaaaaauty"
count=mystring.count("a")
print(count)

#5.string.capitalize
captialize=mystring.capitalize()
print(captialize)

#6.string.upper
upper=mystring.upper()
print(upper)

#6.string.lower
lower=mystring.lower()
print(lower)

#6.string.find(word)
mystring="hello world"
find=mystring.find("e")
print(find)

#6.string.replace(old word,new world)
mystring="hello world"
replace=mystring.replace("h","H")
print(replace)


#escape sequence chracter:
a="hello! i am beauty.\ncould i know about \"you\"?"
print(a)

