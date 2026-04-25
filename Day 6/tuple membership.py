"""
1. What is membership?
👉 Membership means:
👉 “Check if an item exists inside a tuple”
"""
a = (2,3,4,5,)
print(3 in a)
print(7 in a)

invoice_details = ("name", "customer id", "amount paid", )
if "name" in invoice_details:
    print("value found")
else:
    print("value not found")
