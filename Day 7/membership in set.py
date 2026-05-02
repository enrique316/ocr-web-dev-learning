"""
1. What does this mean?
👉 It means:
👉 “Checking whether a value exists in a set”
2. Why this is important
👉 Sets are very fast for checking values
👉 This is one of their biggest advantages
"""

a = {1,2,3,4,5}
if 1 in a:
    print("data found")
else:
    print("value not found")


# another example # 
x = set([1,2,3,4])
print(type(x))

b = {2,3,4}
print(type(b))

y = list({1,2,4})
print(type(y))

xy = [1,2,3,4]
ab = tuple(xy)
print(type(ab))


# ----- # 

dh = {"name", 'address', "phone no"}
print("name" in dh)