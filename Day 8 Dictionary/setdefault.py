"""
1. What is setdefault()?

👉 setdefault() is a dictionary method used to:

“Get a value if key exists, otherwise create the key with a default value”

👉 It combines:

checking
getting
adding default value

into one operation.

2. Basic syntax
dictionary.setdefault(key, default_value)
3. Basic example
d = {
    'name': 'John'
}

print(d.setdefault('name', 'David'))
"""

a = {
    'name': "Shubhankar",
    
}

print(a.setdefault('last','biswas'))