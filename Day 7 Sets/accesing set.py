"""
1. What does this mean?
👉 It means:
👉 “Trying to access items inside a set”
"""
"""
2. Important rule
👉 Sets do NOT support indexing
"""

# check the indexing and picking one index value from set # 

"""a = {1,2,3,4}
print(a[2])"""
"""
4. Why this error happens
👉 Because:
Set is unordered
No fixed position like index 0, 1, 2
👉 So Python cannot find s[0]
"""
"""
6. How to access values in set
👉 You cannot access by index
👉 You must use:
Loop
Membership check
"""
x = {1,2,3,4}
for y in x:
    print(y)

# or using membership method # 
z = set([1,2,3,4])
print(1 in z)