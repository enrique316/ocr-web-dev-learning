"""
1. What is extended unpacking?
👉 Extended unpacking means:
👉 “Capture multiple values using * in a variable”
2. Why we need it?
👉 When number of items is unknown
👉 Or more items than variables
"""

a = (1,2,3,4,5,6)
x, *y,z = a
print(x)
print(y)
print(z)

# another example with ocr # 
invoice_details = ("ABC Limited", "Bandra East.", 70000, True)
name, *other_details, payment_status = invoice_details
print(other_details)


# another example #
ab = (1,2,3,4,5)
*h,i,j,k= ab
print(h)