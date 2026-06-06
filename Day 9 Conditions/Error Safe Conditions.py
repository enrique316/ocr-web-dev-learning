"""
What are Error Safe Conditions?

👉 Error Safe Conditions are conditions written in a way that:

"Prevent the program from crashing."
Real Meaning

Beginners usually write code that assumes data always exists.

Example:

invoice = {
    "amount": 5000
}

print(invoice["vendor"])
What Happens?

Python looks for:

vendor

But vendor does not exist.

Result
KeyError: 'vendor'

💥 Program crashes.
"""

data = {
    "name": "Shubhankar",
    "last_name": "Biswas"
}

if "last_name" in data:
    print("value found")
else:
    print("value not found")


