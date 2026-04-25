"""
1. What is tuple to list conversion?

👉 It means:
👉 “Convert a tuple into a list so we can modify it”
2. Why we need it?
👉 Tuples are immutable
👉 Lists are mutable
👉 So we convert when we want to:
Change values
Add items
Remove items
"""

tuple_1 = (1,2,3,4)
list_1 = list(tuple_1)
print(type(list_1))

# convert to tuple to list and change index 0 index position value # 
name = ("Ram", "Shyma", "Bhat", "lamxman")
name_list = list(name)
name_list[2] = "bharat"
print(name_list)


# from list to tuple with modified data example # 
invoice_data = ["invoice_ID", "customer name", "address", "paid", 7500]
invoice_data[4]= 10000
finale_data = tuple(invoice_data)
print(finale_data)