"""
1. What does this mean?
👉 It means:
👉 “Checking whether two sets have NO common elements”
2. Method used
👉 We use:
isdisjoint()
"""

a = {1,2,3,4}
b = {1,2,3}
print(a.isdisjoint(b))
print(b.isdisjoint(a))

x = {1,2}
y = {3,4}
print(x.isdisjoint(y))

# ocr example # 
name = {"diti", "gauri"}
cats = {"Nadu", "Simba"}
family = name.isdisjoint(cats)
print(family)
