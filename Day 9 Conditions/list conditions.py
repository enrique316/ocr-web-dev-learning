"""
What are List Conditions?

👉 List conditions mean:

“Using conditions to check, validate, filter, or process list items.”
Real Meaning

Instead of checking ONE value:

x = 10

now we work with MANY values together:

[10, 20, 30, 40]
Why This Is Important?

Real systems like OCR and APIs usually process MANY items:

OCR text lines
extracted invoice fields
API records
multiple transactions
document pages

All these are often stored inside LISTS.

2. First Proper Example

Suppose we have skill list.

skills = ["Python", "OCR", "API"]

Now we want to check:

“Does Python skill exist?”
Proper Code Example
skills = ["Python", "OCR", "API"]

if "Python" in skills:
    print("Skill Found")
else:
    print("Skill Missing")
Output
Skill Found
"""
vendor_names = ["Dilip", "Rajesh", "Jitender", "Dharmender"]
if "Dilip" in vendor_names:
    print("Value found")
else:
    print("value Not found")

# Another example # 
amount = [1000, 12340, 2343.4, 10]
if 1 in amount:
    print("found")
else:
    print("not found")

# example with and , or combination # 

extracted_amount = [234, 345, 2343]
invoice_date = ["12jan", "14Jan", "16Jan"]
if 234 in extracted_amount and "12jan" in invoice_date:
    print("true")
else:
    print("false")