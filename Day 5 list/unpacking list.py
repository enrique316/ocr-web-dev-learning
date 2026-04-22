# Unpacking nest list # 
"""
1. What is unpacking?

👉 Unpacking means:

👉 “Take values from a list and store them into variables directly”
"""
"""x = [1,2,3]
a,b,c = x
print(a)
print(b)
print(c)"""

# another example # 

name = ["Diti", "Gauri"]
every_name, some_name = name
print(every_name)
print(some_name)

# another example # 
a = [10, 20, 30]
x, y, z = a
print(x)
print(y)
print(z)

# OCR example # # using looping list #

invoice_data = [['name', 'address'],['phone no','amount']]
for finale_date in invoice_data:
    print(finale_date)