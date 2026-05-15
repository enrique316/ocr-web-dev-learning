"""
1. What is popitem()?

👉 popitem() is a dictionary method used to:

“Remove and return the last inserted key-value pair”

👉 It BOTH:

removes item
returns removed pair
2. Basic syntax
dictionary.popitem()
3. Basic example
d = {
    'name': 'John',
    'age': 25
}

print(d.popitem())
"""

a = {
    'name': 'Diti',
    'address': "hans nagar"

}

print(a.popitem())

# Dictionary after removal # 

x = {
     'name': 'Diti',
    'address': "hans nagar"

}

y = x.popitem()
print(x)
print(type(y))


ab = {
     'name': 'Diti',
    'address': "hans nagar",
    'phone no': True
}

print(ab.popitem())
print(ab.popitem())
print(ab)


# Empty dictionary # 

ax = {

}

print(ax.popitem)

# Access returned tuple values # 

gh = {
     'name': 'Diti',
    'address': "hans nagar",
    'phone no': True
}

j, k = gh.popitem()
print(j)
print(k)