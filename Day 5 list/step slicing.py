# step slicing in list # 
"""
1. What is Step Slicing?
👉 Step slicing is used to skip elements while slicing a list
👉 It adds a third value called step
""" 
a = [1,2,3,4,5,6]
print(a[::2])
print(a[1::2])
# print(a[::0]) # 0 will cause error # 

""" negative revers slicing"""
x = [1,2,3,4,5,6] 
print(x[::-1])

# OCR example # 
data = ["Name", "Address", "Age", "Type"]
print(data[::2])
