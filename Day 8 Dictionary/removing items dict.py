"""
1. What does removing items mean?

👉 Removing items means:

“Deleting key-value pairs from a dictionary”

👉 Sometimes data is:

wrong
temporary
duplicated
invalid

So we remove it from the dictionary.

2. Main ways to remove items
Method	Purpose
pop()	Remove specific key
del	Delete key or whole dictionary
3. Using pop()
Basic syntax
dictionary.pop(key)
"""
a = {
    'name': "jack",
    'last': "sparrow"
}
a.pop("last")
print(a)

# another example # 
x = {
    'place': "manipur" 
}
y = x.pop("place")
print(y)
print(x)

# Now with delete method # 
cd = {
    'invoice': "gfd123",
    'id': 1234
}
del cd["id"]
print(cd)
del cd ["invoice"]
print(cd)