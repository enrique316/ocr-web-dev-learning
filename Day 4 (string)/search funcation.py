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