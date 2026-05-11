"""
1. What does looping dictionary mean?

👉 Looping means:

“Accessing dictionary items one by one automatically”

Great, let’s continue.

Day 8, Chapter 14: Looping Dictionary
1. What does looping dictionary mean?

👉 Looping means:

“Accessing dictionary items one by one automatically”

👉 Instead of manually writing:

print(d['name'])
print(d['age'])
print(d['city'])

we can use loops.

2. Why loops are important

👉 Dictionaries may contain:

hundreds of fields
OCR extracted data
API responses
database records

👉 Loop helps process all data automatically.

3. Basic loop syntax
for key, value in dictionary.items():
    print(key, value)
4. Basic example
d = {
    'name': 'John',
    'age': 25,
    'city': 'Delhi'
}

for key, value in d.items():
    print(key, value)
"""

x = {
    'name': "Shubhankar",
    'Last':"biswas",
    'age': 39
}

for key, value in x.items():
    print(key, value)

# another example # 

a = {
    'name': "Shubhankar",
    'Last':"biswas",
    'age': 39
}

for key,value in a.items():
    print(key, value)

# if we want to loop only key or value from the dictionary # 

for key in a:
    print(key)

for value in a:
    print(value)

    