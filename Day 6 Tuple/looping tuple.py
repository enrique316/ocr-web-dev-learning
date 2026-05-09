"""
1. What is looping?
👉 Looping means:
👉 “Go through each item one by one”
2. Why we use it?
👉 To process all values in a tuple
👉 Instead of accessing manually
"""

a = (1,2,3)
for b in a:
    print(b)

# another example # 

x= ("dimpal", "pimpal", "simple")
for y in x:
    print(y)

# another example # 

ab = (1,2,3,4,5)
for cd in range(len(ab)):
 print(ab[cd])

# Another example with OCR # 
invoice_details = ("invoice_ID", "Customer Name", "Address", "Phone No")
for data in range(len(invoice_details)):
   print(invoice_details[data])

# another example # 

ty = ("name", "age", "country")
for gh in range(len(ty)):
   print(gh,ty[gh])