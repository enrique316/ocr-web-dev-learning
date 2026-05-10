"""
1. What does creating dictionary mean?

👉 Creating a dictionary means:

“Making a key-value data structure”

👉 Dictionary stores data like this:

key : value

Example:

'name' : 'John'
'age' : 25
2. Two main ways to create dictionaries

Python mainly provides:

Method	Syntax
Curly braces	{}
dict() function	dict()
"""
# basic style #
a = {
    'name': "Shubhankar"
}
print(a)

#using dict() method #
x =dict(name='Diti', age=11)
print(type(x))
print(x)

ab =dict(country='india', from_list=True)
print(ab)