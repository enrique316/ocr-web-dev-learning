"""
What are Condition Functions?

👉 Condition functions are built-in Python functions that help us make decisions.

Instead of writing long conditions manually, Python provides functions that return:

True

or

False
Most Common Condition Functions
Function	Purpose
bool()	Convert value to True or False
all()	Check if ALL values are True
any()	Check if AT LEAST ONE value is True
Why Are They Useful?

Suppose an OCR system extracts:

invoice_no = "INV001"
vendor = "Amazon"
amount = 5000

We need to know:

Are all fields present?
Is at least one field present?
Is a field empty?

Condition functions make this easy.

2. Understanding bool()

bool() converts any value into:

True

or

False
Example 1
print(bool("Python"))

Output:

True
Why?

Python checks:

"Python"

Is the string empty?

No.

Therefore:

True
"""
x = 2
print(bool(x))

# example # 

invoice_id = "INZV345"
vendor_name = "FlipkartIND"
amount = 500000
print(all([invoice_id, vendor_name, amount]))
print(any([invoice_id, vendor_name, amount]))

if bool(invoice_id):
    print("data found")
else:
    print("data not found")


age = {10, 0, True}
print(all(age))
print(any(age))

age1 = [19, 20, 21]
print(all(age1))
print(any(age1))

# ocr examples#
extracted_ven_name = ""
extracted_ven_amount = 50000
extracted_ven_address = "NYC"
if all([extracted_ven_amount, extracted_ven_address, extracted_ven_name]):
    print("data valid")
else:
    print("data not valid")

if any([extracted_ven_amount, extracted_ven_address, extracted_ven_name]):
    print("Data found")
else:
    print("data not found")