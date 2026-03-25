# Search function # 
"""
find()
rfind()
index()
rindex()
"""
name = "My Name is Diti"
print(name.find("Diti"))

# if the index value isnt present #
invoice_name = "ADJ Associates PVT. ltd"
print(invoice_name.find("hi"))

# .find vs .index #
x = " my name is ABC"
print(x.find("z"))

# but with .index #
"""b = " He is good"
print(b.index("She")) """

# 7. Reverse Search using rfind() # 
name_1 = "He is a Good Jolly But Not Good Jolly"
print(name_1.rfind("Jolly"))

# example with index # 
name_a = " How do you find the How but "
print(name_a.index("How"))

# example index with error output #
"""
f = " he is good man"
print(f.index("she")) """

#  example .rindex #
f = "He is a good man"
print(f.rindex("He"))

# OCR examples #
invoice_data = " INV20-09-2007: JB Jewellers"
captured_data = invoice_name.find("JB Jewellers")
print(captured_data)

# Another example #
invoice_value = " ABC: 600"
value_data = invoice_value.find(":")
print(invoice_value[value_data+ 1:])

# Another example #
a = " Data is 5006"
if a.find("value") == -1:
    print("data not found")
else:
    print("data found")
