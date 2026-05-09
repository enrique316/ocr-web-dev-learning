"""
1. What does this mean?
👉 It means:
👉 “Checking if all elements of one set exist inside another set”
1. What does this mean?
👉 We use:

issubset()

"""

a = {1,2,3,4}
b = {1,2,3}
print(a.issubset(b))
print(b.issubset(a))

# example with issubset() # 

invoice_details1 = {"invoiceID", "Invoice_Name", "Date", "Amount","Address"}
invoice_details2 = {"Invoice_Name", "Date", "Amount","Address"}
final_data = {invoice_details1.issubset(invoice_details2)}
print(final_data)

"""
6. Important understanding

👉 Smaller set inside bigger set:

{1,2} ⊆ {1,2,3}
"""
"""
Using operators
👉 Another way:
"""
x = {1,2,3,4}
y = {1,2,}
z = x <= y
print(z)

