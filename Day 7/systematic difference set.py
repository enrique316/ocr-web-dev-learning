"""
1. What does this mean?
👉 It means:
👉 “Finding values that are in either set, but NOT in both”

👉 We use:
^
👉 Or:
symmetric_difference()


"""

a = {1,3,4,5,}
b = {2,3,6}
d = a^b
print(d)

# using symmetric_difference() method # 
x = {1,3,2,34}
y = {5,6,3,2}
print(x.symmetric_difference(y))

"""
6. Important understanding

👉 Formula:

(A ∪ B) - (A ∩ B)

👉 Meaning:

Union minus intersection
"""
# OCR examples # 

invoice_details = {"Invoice_ID", "Amount", "Date", "Discount"}
invoice_details_2 = {"amount", "Place"}
print("difference:", invoice_details^invoice_details_2) 