"""
1. What is count()?
👉 count() means:
👉 “Count how many times a value appears in a tuple”
"""
a = (1,2,3,4,5,3,3,3,3,34,5)
print(a.count(3))

# another example # 
name = ("diti", "gauri", "gauri", )
find = name.count("gauri")
print(find)


data = ("name", "name","name","name", "last name", "last name")
if data.count("name") == 4:
    print("data valid")

