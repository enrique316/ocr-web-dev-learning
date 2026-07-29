# What is loop with funcation # 
"""
Instead of writing the same code multiple times, you create a function once and let the loop call it for each item.

This makes your code:

Easier to read
Easier to maintain
Reusable
Less repetitive
"""
"""
def greet():
    print("welcome")

for i in range(2):
 greet() """ 
"""
def hi():
    print("say Hello")
for y in range(4):
    hi() """ 
# OCR example # 

def ocr_processing(data):
    print("processing:", data)

invoice = [
     "INV1",
     "INV2",
     "INV3"
    ]
for x in invoice:
    ocr_processing(x) 
""" 
def dimpal():
    first_name = "Shubhankar"
    first_name += "biswas"
    print(first_name)




dimpal() """ 