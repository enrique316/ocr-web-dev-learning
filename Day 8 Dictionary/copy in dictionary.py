"""
1. What does copying dictionary mean?

👉 Copying means:

“Creating another dictionary from an existing dictionary”

👉 Python provides two important ways:

Method	Behavior
Assignment	Shares same dictionary
copy()	Creates separate dictionary
2. Assignment copy
Example
d1 = {
    'name': 'John',
    'age': 25
}

d2 = d1

print(d1)
print(d2)
"""
a = {

    'name': "Dimpeee",
    'last_name':"Roy",
}

b = a

print(a)
print(b)

# 

x = {
    'date': "17May2030"
}


# Similar solution with .copy method # 

y = x.copy()
print(y)
