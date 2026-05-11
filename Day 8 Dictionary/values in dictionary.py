"""
1. What is values()?

👉 values() is a dictionary method used to:

“Get all values from a dictionary”

👉 It extracts only values.

NOT keys.

2. Basic syntax
dictionary.values()
3. Basic example
d = {
    'name': 'John',
    'age': 25,
    'city': 'Delhi'
}

print(d.values())

👉 Output:

dict_values(['John', 25, 'Delhi'])
"""

a = {
    'name':"Shubhankar",
    "age": 38
}

print(a.values())

a['city'] = "rewari"

print(a.values())
y= list(a.values())

print(y)