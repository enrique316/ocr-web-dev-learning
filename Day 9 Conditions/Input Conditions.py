"""
What are Input Conditions?

👉 Input conditions mean:

"Taking input from the user and making decisions based on that input."

Up to now, we were manually creating variables:

age = 25

But real programs work like this:

age = int(input("Enter your age: "))

The user enters the value.

Then Python decides what to do.

Why Is This Important?

Real systems receive input from:

Users
OCR engines
APIs
Databases
Forms

Python must validate that input before using it.

2. First Proper Example

Suppose user enters age.

age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")
Sample Run
User enters:
20
"""
"""name = str(input("Customer Name:"))
age = float(input("Age:"))
country = str.lower(input("Country:"))
invoice_ID = str(input("Invoice ID:"))
amount = float(input("amount:"))
if country == "india" and amount > 5000: 
    print("invoice accepted")
else:
    print("invoice rejected")"""

# example # 

""""age1 = float(input('enter your age:'))
city = str(input("enter your state:")).strip().casefold()
if age1 > 18 and city == "delhi": 
    print("verified")
else:
    print("not verified") """

# another example with membership condition # 

extracted_date = input("enter date:").casefold()
if "jan" in extracted_date: 
    print("value found")
else:
    print("value not found")

