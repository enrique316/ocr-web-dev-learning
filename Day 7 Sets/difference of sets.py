"""
1. What does this mean?
👉 It means:
👉 “Finding values that exist in one set but NOT in another”
2. Operator used
👉 We use:

-

👉 Or:

difference()
"""

a = {1,2,3,4}
b = {3,4,7}
c = (a-b)
print(c)

# another same example # 
ab = set([2,3,4,5])
bc = set({2,3,7})
print(ab-bc)

# using difference method # 
x = {2,3,4,5}
y = {2,36}
print(a.difference(y))



