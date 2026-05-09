"""
Day 6, Chapter 6: Slicing Tuples
1. What is slicing?
👉 Slicing means:
👉 “Extract a part of a tuple”
([]:[])
"""
x = (1,2,3,4,5,)
print(x[1:4])

#try another example # 

a = (2,5,6,8)
b = (a[0:3])
print(b)

# lets try with negative index # 
xy = (1,2,3,4,5,6)
ab = (xy[0:-2])
print(xy[1:])
print(xy[:2])
print(xy[:])
print(ab)

# OCR example # 

invoice_data = ("name", "address", 7000, True)
print(invoice_data[-1:-2])
print(invoice_data[:])

