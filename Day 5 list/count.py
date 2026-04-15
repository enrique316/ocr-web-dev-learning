# count() in list # 
"""1. What is count()?
👉 count() is used to count how many times a value appears in a list
👉 It returns a number (frequency) """

list_1 = [1,1,1,1]
print(list_1.count(1))

# another example # 
x = [1,2,1,2,3,4,2]
print(x.count(2))
print(x.count(6))

# index vs count in list # 
# index provide index position value while count provide time  numbers of time an unique value as appear in the list # 
a = [1,2,3,1,1,2,3,11]
print(a.count(2))
print(a.index(1))

# detect duplicate values # 
x_1 = [1,2,1,2,3,4,2,4,2]
if x_1.count(2)> 2:
    print("Duplicate found")
else:
    print("duplicate not found")

# OCR examples # 
items_details = ["adiads", "nike", "puma", "kappa", "adidas", "nike", "nike"]
print("total nike pairs:", items_details.count("nike"))