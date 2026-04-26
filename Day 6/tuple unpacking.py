"""
1. What is tuple unpacking?
👉 Tuple unpacking means:
👉 “Assign tuple values to variables”
"""

a = (1,2,3)
x,y,z = a
print(x,y,z)

# Another example # 
name = ("Dimpal", "Diti", "Kanika")
Mom, Daughter1, Daughter2 = name
print(Mom, Daughter1 , Daughter2)

#ocr example # 

Invoice_data = ("Shubhankar", "rewari", 941634567)

name, address, phone_no = Invoice_data
print(phone_no)
print(address)
