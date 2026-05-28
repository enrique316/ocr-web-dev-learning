"""
What are Dictionary Conditions?

👉 Dictionary conditions mean:

“Using conditions to validate, search, or check data inside dictionaries.”
Real Meaning

Earlier you learned:

data = {
    "name": "John",
    "age": 30
}

That chapter focused on:

creating dictionaries
accessing values
updating keys

Now this chapter focuses on:

“Checking whether required keys or values exist.”
Why This Is Important?

Real systems like:

OCR
APIs
AI systems
databases
automation tools

mostly store data in dictionary format.

Real OCR Example

OCR engines often return data like this:

invoice = {
    "invoice_no": "INV001",
    "amount": 5000,
    "vendor": "Amazon"
}

Now system must validate:

invoice number exists
amount exists
vendor exists

This is where dictionary conditions are used.

2. First Proper Example
data = {
    "name": "John",
    "age": 30
}

if "name" in data:
    print("Key Found")
else:
    print("Key Missing")
Output
Key Found
"""

name = {"diti", "Gauri", }

if "diti" or "Gauri" in name:
    print("true")
else:
    print("false")

name = {
    "first_name": "John",
    "second_name": "Paul"
}

if "first_name" in name:
    print("true")
else:
    print("false")
# Another example # 
extracted_data = {
    "x": 2000,
    "y": 500,
    "name1": "John Paul",
    "name2": "Pamela"
    }
print(type(extracted_data))
if "x" in extracted_data and "name2" in extracted_data:
    print("true")
else:
    print("false")

# another example #

captured_value = {
    "value1": 7000,
    "Value2": 5600,
    "address": "LA",
    "Address2": "SF"
}

if "address" in captured_value and captured_value["value1"]> 6000:
    print("data valid")
else:
    print("data invalid")