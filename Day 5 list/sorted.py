# sorted() in list # 
"""
1. What is sorted()?
👉 sorted() is used to sort a list and return a new list
👉 It does NOT change the original list
"""
x = [2.1, 1, 3, 7, 4]
b = sorted(x)
print(b)

# Another example # 

a = ["Jack", "Monica", "Amanda", "Paul"]
y = sorted(a)
print(y)

# OCR example # 

invoice_data = ["INV-12345", "Age", "Address", "types", "Date"]
filtered_data = sorted(invoice_data)
print("Final Data:", filtered_data)