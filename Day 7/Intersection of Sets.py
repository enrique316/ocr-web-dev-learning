"""
1. What does this mean?
👉 It means:
👉 “Finding common values between two sets”
2. Operator used
👉 We use:
&

👉 Or:
intersection()

5. How it works
👉 Compares both sets
👉 Keeps only values present in both
👉 Removes everything else
"""
a = {1,2,3}
b = {2,4,1}
print(a&b)
# or you can try this method# 
print(a.intersection(b))


# another example #

x= {1,2,3}
y = {2,3}
z= x&y
print(z)