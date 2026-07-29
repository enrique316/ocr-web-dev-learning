# What is zip in python #
""" 
The zip() function is used to combine two or more collections (lists, tuples, etc.) so that you can loop through them at the same time.

Imagine you have two separate lists:

One list contains student names.
Another list contains their marks.

Instead of looping through each list separately, zip() joins them together.
"""

""" 
name = ["diti", "gauri", "jaggu"]
marks_obtained = [78, 98, 76]

for names, mark in zip(name, marks_obtained):
    print(names, "-", mark) """ 

fields = ["Name", "Address", "Amount"]
data = ["XYZ industries", "Florida", "$12323434"]
for x, y in zip(fields, data):
    print(x, ":", y) 

#-----# 

name = ["diti", "gauri", "jaggu"]
marks_obtained = [78, 98, ]
for a,b in zip(name, marks_obtained):
    print(a,":", b)