"""
1. What is list comprehension?
👉 List comprehension means:
👉 “Create a new list using a short and simple syntax”
"""
""" before we start learning the main topic we need to understand what is append in python as it is very/ 
important for learning the list """ 

"""a = [1,2]
a.append(2)
print(a)"""


"""x = [1,2,3,4]
x.append(x[0])
print(x)"""


#Now proceed with list comprehension # 
y =[1,2,3,4]
x = []
for z in y:
    x.append(z*2)
    print(x)