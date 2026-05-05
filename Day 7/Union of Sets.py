"""
1. What does this mean?
👉 It means:
👉 “Combining two sets into one set with all unique values”
2. Operator used
👉 We use:

|

👉 Or:
union()
"""

a = {1,2,3}
b = {4,5,6}
c = (a|b)
print(c)

# Using union method # 
# -- Important -- # 
"""x = set(1,2)
y = set(3,4)
z= (x.union(y))
print(z)"""  # This method would work , Try # 

x = {1,2}
y = {3,4}
print(x.union(y))

#or you can try #
x = set([1,2])
y = set([3,4])
z= (x.union(y))
print(z)