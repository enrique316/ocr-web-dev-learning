"""
1. What is Ternary Operator?

👉 Ternary operator is a SHORT one-line version of:

if else

Instead of writing:

if condition:
    value1
else:
    value2

    Important Understanding

Python reads ternary operator like this:

IF condition is True
THEN return left value
ELSE return right value
"""
a = 10 
print("yes" if a > 5 else "No" )
print("yes" if a > 12 else "NO")

# age verification method example # 
age = 23
verification_status = "yes" if age > 18 else "You must be 18+ to access the page"
print(verification_status)