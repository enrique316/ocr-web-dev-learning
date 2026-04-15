# index in list # 
"""
1. What is index()?
👉 index() is used to find the position of a value in a list
👉 It returns the index number of the first match
"""
x = [1,2,3,4]
print(x.index(3))
# another example # 

a = [23.45, 345.4, ]
print(a.index(23.45))

# now lets try with string # 
b = ["name","address", "age"]
print(b.index("age"))

# safe method # 

xy = [1,2,3,4]
if 2 in xy:
    print(xy.index(2))
else:
    print("data error")

# what if the same value is twice and thrice time repeating # 

vx = [2, 1, 2, 3]
if 2 in vx:
    print(vx.index(2))
else:
    print("data not found")


# OCR examples # 

invoice_details = ['invoice ID', ' Customer name', 'Address', 567000]
if 'Customer name' in invoice_details:
    print(invoice_details.index('Customer name'))
else:
    print("Data not found")

# another OCR example # 
details = ["invoice ID", "customer name", 6000, "12-Jan-2027"]
if "customer name" in details:
    set_postion = details.index("customer name")
    print("customer name index found:", set_postion)

