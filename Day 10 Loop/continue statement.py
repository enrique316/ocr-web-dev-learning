"""
1. What is the continue Statement?

👉 The continue statement skips the current iteration of a loop and moves directly to the next iteration.

Unlike break:

break → Stops the entire loop.
continue → Skips only the current item and continues with the remaining items.
Real Meaning

Suppose you are processing OCR fields:

Invoice No
Vendor
(empty)
Amount
Date

You don't want to stop processing because of one empty field.

Instead, you want to:

Skip empty field
Continue processing remaining fields

That's exactly what continue does.

2. First Example
Code
for i in range(5):

    if i == 2:
        continue

    print(i)
Output
0
1
3
4
"""
"""
for y in range(6):
    if y == 2:
        continue
    print(y) """

"""
for z in range(4):
 if z ==1:
    continue
 print(z) """ 

extracted_data = ["name", "address", "amount", "date"]

for name in extracted_data:
    if name == "name":
        continue
    print(name)

# Skip Negative Numbers # 
numbers = [1,2,3,-6,-7]
for numbers in numbers:
    if numbers <0:
        continue
    print(numbers)