# extend in list # 
"""1. What is extend()?
The extend() method means:
👉 Adding multiple items to a list
👉 Merging another list into the current list
Unlike append(), it does not add as a single item. It adds each element one by one."""

name = ["ram","shyam"]
name.extend(["Sita", 12])
print(name)

#6. Using extend() with Different Data Types# """ passing a string in list with .extend"

list_1 = [1]
list_1.extend("hi")
print(list_1)

# using tuple #

new_list = [1]
new_list.extend((1,2))
print(new_list)

# with sets {} #
list_2 = [1]
list_2.extend({1,3})
print(list_2)

# OCR examples # 

invoice_details = ["INV345t", 5600]
leftout = ["12-Jan26", True]
invoice_details.extend(leftout)
print(invoice_details)