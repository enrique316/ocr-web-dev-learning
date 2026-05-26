"""
What is Boolean Logic?

👉 Boolean logic means:

“Working with True and False values”

Python internally makes decisions using ONLY:

True
False
Important Understanding

Almost every condition in Python finally becomes:

True
or
False
Real Meaning

Boolean logic is the FOUNDATION of:

if statements
AI systems
OCR validation
APIs
fraud detection
automation
decision engines
2. What is a Boolean Value?

Boolean values are special data types.

Python has ONLY TWO Boolean values:

True
False
Proper Example
print(True)
print(False)
Output
True
False
3. Boolean Type Checking

Boolean values have their own datatype.

Proper Example
print(type(True))
"""

actual_amount = 10000
extract_amount = 8900
print(actual_amount > extract_amount)
print(extract_amount > actual_amount)
if actual_amount != extract_amount:
    print(True)
else:
    print(False)

# example # 
print(bool(1))
print(bool(0))

# bool(1) and bool(0) example #

invoice_1 = 1000
invoice_2 = 2000
invoice_3 = ""
if invoice_1 and invoice_2 and invoice_3:
    print("data found")
else:
    print("data not found")

# another example # 
dealer_name = ""
address = "Huston, TX"
print(bool(dealer_name))
print(bool(address))