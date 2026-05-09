"""
1. What does this mean?

👉 A frozenset is an immutable version of a set
👉 Meaning:
Values cannot be changed
Cannot add items
Cannot remove items
2. Why frozen set exists
👉 Normal sets are mutable
s = {1, 2}
s.add(3)

👉 Allowed

👉 But sometimes we need:

Fixed data
Secure data
Unchangeable collections

👉 So Python provides:

frozenset()
3. Basic example
fs = frozenset([1, 2, 3])

print(fs)
7. Why frozenset is useful

👉 Can be used:

As dictionary keys
Inside another set
For secure constant data
"""
a = frozenset([1,2,3,4])
print(a)

