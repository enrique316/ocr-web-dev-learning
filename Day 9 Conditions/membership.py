"""
1. What are Membership Operators?

👉 Membership operators are used to check whether something EXISTS inside another object.

Python mainly uses:

Operator	Meaning
in	Check if value exists
not in	Check if value does NOT exist
Real Meaning

Membership operators answer questions like:

Does this word exist?
Does this key exist?
Does this item exist?
Why Membership Operators are Important?

Real systems constantly check:

if OCR extracted required fields
if invoice contains total amount
if API response contains status
if user exists in database
if product exists in inventory
2. First Proper Example Using in
data = "Invoice Total Amount"

print("Total" in data)
Output
True
"""
extracted_data = " 1000 in invoice"
print("1000" in extracted_data)

print_message = "amount found in bill"
if "amount" in print_message:
    print("data found")
else:
    print("data not found")