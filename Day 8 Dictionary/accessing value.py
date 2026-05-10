"""
1. What does accessing values mean?

👉 Accessing value means:

“Getting data from dictionary using its key”

👉 Dictionaries do NOT use index positions like lists.

❌ Wrong:

d[0]

✅ Correct:

d['name']
2. Basic syntax
dictionary[key]

👉 Example:

d = {
    'name': 'John',
    'age': 25
}

print(d['name'])
"""

ab = {
    'name': "Dimapl",
    'last_name': "Roy",
    'age': 100
}
print(ab['age'])
# accessing multiple values#
print(ab['last_name'])

# Accessing different data types # 
#String value# , integer 
cd = dict(name="Diit")

# accessing list values #

a = {'marks':[90, 70, 70]}
print(a['marks'])
print(a)
