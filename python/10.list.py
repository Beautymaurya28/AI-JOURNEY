#list indexing
friends=["apple","orange",5,345.6,False,"Aakash","Rohan"]
friends[0]="grapes"
print(friends[0])
print(friends[1:4])

#list methos

#1.sort()=updates the string in increasing order
l1=[4,8,2,9,5]
l1.sort()

#2.reversed()=reverse the list
l1.reverse()
print(l1)

#3.append=add the another value in the last of strings
l1.append("beauty")
print(l1)

#4.insert=add any value at any index in list
friends=["apple","orange",5,345.6,False,"Aakash","Rohan"]
friends.insert(3,"banana")
print(friends)

#5.pop
print(l1.pop(3))

