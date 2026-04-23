"""
1. What are the ways to create a tuple?
👉 There are 2 main ways:

Using ()
Using tuple()

👉 When data is already in another format like:
list
string
"""
x = (1,2,3)
print(x)

# convert a list into a tuple # 
a = tuple([1,2,3,4])
print(a)

# example with string # 
name = "shubhankar"
name=tuple("shubhankar")
print(name)

# ocr example # 
invoice_data = ["name", "address", 7000, True]
refined_data = tuple(invoice_data)
print(refined_data)
