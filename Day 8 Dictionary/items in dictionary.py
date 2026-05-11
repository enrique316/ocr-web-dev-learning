"""
1. What is items()?

👉 items() is a dictionary method used to:

“Get both keys and values together”

👉 It returns:

(key, value)

pairs.

2. Basic syntax
dictionary.items()
3. Basic example
d = {
    'name': 'John',
    'age': 25
}

print(d.items())

👉 Output:

dict_items([('name', 'John'), ('age', 25)])
"""

yx = {
    'invoiceid': "DGC123",
    'date': '12Jan2026'
}
print(yx.items())

cd = {
    'Name': "Johny Cage",
    'series': "Mortal Combat",
    'year': 1992,
    'available': True 
}

print(cd.items())
