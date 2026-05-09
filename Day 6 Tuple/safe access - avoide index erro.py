"""
1. What is safe access?
👉 Safe access means:
👉 “Access tuple values without causing errors”
"""

# we try # 
""" ac = (1,2,3)
print(ac[5]) """ """ this will give you error as index is out of range"""

# with safe access - basic # 
ac = (1,2,3)
if len(ac)> 2:
    print([2])
else:
    print("index position not available")


# another example with ocr # 
invoice_details = ("account number", "amount", "date of invoice", "address")
if "account number" in invoice_details:
    print("data found")
else:
    print("data not found")