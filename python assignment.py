#list,type
l=[3,4,5]
print(l)
print(type(l))
#append
l=[3,4,5]
l.append(6)
print(l)
#sort
l=[11,23,3,4,5]
l.sort()
print(l)
#reverse
l=[11,23,3,4,5] 
l.reverse()
print(l)
# index
l=[11,23,3,4,5]
print(l.index(4))
print(l)
# count
l=[14,24,34,4,5]
print(l.count(1))
print(l)
#copy
l=[14,24,34,4,5]  
m=l.copy()
m[0]=0
print(l)
#insert
l=[14,24,34,4,5]
l.insert(1,899)
print(l)
#extend
l=[14,24,34,4,5]
m=[900,700,300]
l.extend(m)
print(l)
# length of the list
l=[11,23,3,4,5]
print(len)
print(l)
# max in list
m=max(2,9,1)
print(m)
# min in list
m=min(2,9,1)
print(m)
# copy list
z = ["apple", "banana", "cherry"]
list = z.copy()
print(list)
# Sort List Alphanumerically
m = ["red", "blue", "green", "orange", "purple"]
m.sort()
print(m)
#Loop Through a List
m= ["green", "red", "blue"]
for x in m:
  print(x)
#Join Two Lists
list1 = ["a", "b", "c" ]
list2 = [1, 2, 3]
list3 = [list1 + list]
print(list3)

# Python Dictionaries
dict =	{
  "brand": "borjan",
  "model": "girl b",
  "year": 1992
}
print(dict)

# Dictionary Items
dict = {
  "brand": "borjan",
  "model": "Girl B",
  "year": 1994
}
print(dict["brand"])

# Dictionary Length
dict={
"brand": "borjan",
"model": "Girl B",
"year": 1994,
}
print(len(dict))

# Accessing Items
dict ={
  "brand": "borjan",
  "model": "Girl b",
  "year": 1964
}
m =dict["model"]
print(m)

# Get Keys
dict = {
  "brand": "Ford",
  "model": "girl b",
  "year": 1964
}
m= dict.keys()
print(m)

# Update Dictionary
dict = {
  "brand": "borjan",
  "model": "the girls",
  "year": 1998
}
dict.update({"year": 2015})

# Adding Items
dict = {
  "brand": "borjan",
  "model": "the girls",
  "year": 1998
}
dict["color"] = "red"
print(dict)

# Removing Items
dict = {
  "brand": "borjan",
  "model": "the girls",
  "year": 1998
}
dict.pop("model")
print(dict)

# Copy a Dictionary
dict = {
  "brand": "borjan",
  "model": "the girls",
  "year": 1998
}
dict = dict.copy()
print(dict)

# Nested Dictionery
family = {
  "child1" : {
    "name" : "noor",
    "year" : 2000
  },
  "child2" : {
    "name" : "tuba",
    "year" : 2002
  },
  "child3" : {
    "name" : "zain",
    "year" : 2006
  }
}

print(family)

