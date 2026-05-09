"""
1. What does this mean?
👉 It means:
👉 “Checking if one set contains all elements of another set”
2. Method used
👉 We use:
issuperset()
5. How it works internally

👉 Python checks:

Does first set contain every item of second set?

👉 If yes → True
👉 Else → False
6. Important understanding

👉 Bigger set containing smaller set:

{1,2,3} ⊇ {1,2}
"""
a = {1,2,3,4}
b = {1,2,3}
print(a.issuperset(b))

"""
7. Using operators
👉 Another way:
>=
"""
x = set([1,2,3,4])
print(type(x))
y = set([1,2])
z = x>=y
print(z)

