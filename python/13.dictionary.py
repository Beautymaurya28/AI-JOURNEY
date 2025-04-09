marks={
    "beauty":100,
    "rohan":56,
    "vivek":76,
}

print(marks)
print(type(marks))
print(marks["beauty"])


#dic methods
#1.marks.itmes():
marks={
    "beauty":100,
    "rohan":56,
    "vivek":76,
}
print(marks.items())

#2.marks.keys():
print(marks.keys())

#3.marks.updates():
marks.update({"beauty":99,"rohan":70})
print(marks)

#4.marks.get("name")
print(marks.get("beauty"))
print(marks.get(70))

#5.marks.pop()
print(marks.pop("rohan"))
print(marks)

