# Copy list# 
"""
1. What is Copying a List?
👉 Copying means creating a new list from an existing list
👉 Important because lists are mutable (changeable)
"""

a = [1,2,3,4]
b= a.copy()
print(b)
# another example # 
x = ["apple", "banana", 1.45, True]
print(x.copy())

# Another way to copy # 

name = ["ram", "shyam"]
b = name[:]
print(b)