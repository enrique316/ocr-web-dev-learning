"""
1. What does this mean?

👉 It means:
👉 “Adding a new value into a set”
2. Method used
👉 We use:
add()
"""

a = {1,2,3,3,5}
a.add(4)
print(a)

#------# 
xy = {"name", 70000, True}
xy.add(False)
print(xy)

# you cant add multiple values at once, for that you need to use update() method. # But you can try - # 
invoice_data = {"name"}
invoice_data.add("invoice_Id")
invoice_data.add(560000000)
print(invoice_data)
