"""

Day 8, Chapter 21: update() Method
1. What is update()?

👉 update() is a dictionary method used to:

“Add or merge key-value pairs into a dictionary”

👉 It can:

add new keys
update existing keys
merge dictionaries
2. Basic syntax
dictionary.update(other_dictionary)
3. Basic example
d = {
    'name': 'John'
}

d.update({
    'age': 25
})

print(d)
"""

a = {
    'name':"diti"
    }
a.update({'another_name': 'Kanika'})
print(a)

# Updating existing key or pair? #

b = {
    'class_3rd': "kanika",
    'class_6th': "diti" 
}

b.update({'class_6th':"diti Biswas"})
print(b)

#you can add multiple keys #  

# merge two directories # 

ab = {
    'name': "Kanika"
}

cd= {
    'class': "3rdrose"
}

ab.update(cd)
print(ab)


# This doesnt work # 
"""
d = {
    'name': 'John'
}

x = d.update({'age': 25})

print(x)
"""
