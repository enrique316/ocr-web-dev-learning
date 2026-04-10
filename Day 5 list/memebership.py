# membership in list # 
"""
1. What is Membership?
Membership means checking:
👉 Does a value exist inside a list or not?
Python gives a simple way to do this using:
👉 in
👉 not in
"""
list_1= [1,2,3,4]
print(2 in list_1)

# another example with string value # 

a = ["name", "last name","age"]
print("name" in a)


# another example # 

x_a = [1,2,"Name", "age"]
print(2 not in x_a)

# ocr example #
invoice_data = ["name", "a", 3450, "INVOICE-12"]
if "INVOICE-12" in invoice_data:
    print("data valid")
else:
    print("data not valid")