# Using .clear in list # 
"""
1. What is clear()?
clear() is used to remove all items from a list.
👉 After using clear(), the list becomes empty, but the list itself still exists in memory.
"""

list_1 = [1,2,3,4]
list_1.clear()
print(list_1)

# another example # 
"""invoice_details = ["Name", "Address", 7000, False]
invoice_details.clear("address")
print(invoice_details)""" # this woudnt work as you cant pick a index positon or value from the list and delete it# 
#with .clear() you can delete entire items from the list # 

