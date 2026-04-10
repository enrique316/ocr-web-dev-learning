# using del in list .del() # 
"""
1. What is del?
del is used to:
👉 Delete elements using index
👉 Delete multiple elements
👉 Even delete the entire list
👉 Important:
del does NOT return any value
"""

x = [1,2,3,4]
del x[0]
print(x)

# some other examples # 
list_1 = ["name", "last name", "address"]
del list_1[1]
print(list_1)

# Delete Multiple Elements (Slicing) # 

name = ["Shubhankar","Dimapl","Diti","Gauri"]
del name[3]
del name[1]
print(name)

# del vs remove vs pop # 
x_1 = [1,2,3,4]
del x_1[0]
x_1.remove(2)
x_1.pop(0)
print(x_1)

