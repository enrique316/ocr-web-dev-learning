"""
1. What is index()?
👉 index() means:
👉 “Find the position of a value in a tuple”
"""

a = (1,2,3,4)
print(a.index(2))

# another example # 
b = ("name", "address", "phone no")
print(b.index("address"))


# example while there are two similar values in the tuple #
invoice_details = ("name", "address", "amount", "name")
print(invoice_details.index("name")) # The outcome will be 0 # 