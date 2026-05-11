"""
1. What is keys()?

👉 keys() is a dictionary method used to:

“Get all keys from a dictionary”

👉 It extracts only field names.

NOT values.

2. Basic syntax
dictionary.keys()
3. Basic example
d = {
    'name': 'John',
    'age': 25,
    'city': 'Delhi'
}

print(d.keys())

👉 Output:

dict_keys(['name', 'age', 'city'])
Why output looks strange?

👉 Because Python returns a special object called:

dict_keys

👉 It is a dynamic view of dictionary keys.
"""

a = {
    'name':"Shubhankar",
    'last_name':"Biswas",
    'Age': 17,
    "City": "Rewari"
}
print(a.keys())

#Convert keys into list#
b =list(a.keys())
print(type(b))
a['amount'] = 5000
print(a)
