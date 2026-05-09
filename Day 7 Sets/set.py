"""
1. What does this mean?
👉 A set is a collection of values where:
Order does not matter
Duplicate values are not allowed

2. Why sets are important?
👉 Because they automatically:
Remove duplicates
Store only unique values
Provide fast lookup

5. Key characteristics
👉 Set properties:
No duplicate values
No indexing
Unordered
Mutable

"""

a = {1,2,3}
print(a)

x = {"name", "address", "name", "Name"}
print(x)

# indexing in sets # 

""" print(a[0]) indexing doesnt work with sets """ 
invoice_details = ["name", "address", "phone no", "address", "amount"] 
clean_data = set(invoice_details)
print(clean_data)

