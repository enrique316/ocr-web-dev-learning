"""
What are Set Conditions?

👉 Set conditions mean:

“Using conditions to validate, search, or check items inside sets.”
Real Meaning

A set is mainly used when:

“Only unique values are allowed.”
Why Sets Are Important?

Real systems often need to remove duplicates.

Examples:

duplicate OCR fields
repeated invoice numbers
repeated API IDs
duplicate users
repeated transactions

Sets help validate uniqueness quickly.

2. First Proper Set Example
data = {"Python", "OCR", "API"}

if "Python" in data:
    print("Skill Found")
else:
    print("Skill Missing")
Output
Skill Found
"""
name = {"ram", "Shyam", 'Vinod'}
last_name = {
    "first1": "ram",
    "First2": "Shyam",
    "First3": "Vindod" 

}

print(type(name))
print(type(last_name))
print(type(name),type(last_name))
if "ram" in name:
    print("true")
else:
    print("false")

# Another example # 
invoice_numbers = [
    "inv1",
    "inv2",
    "inv2",
]
print(type(invoice_numbers))
if len(invoice_numbers) != len(set(invoice_numbers)):
   print("Duplicates found")
else:
   print("duplicates not found")