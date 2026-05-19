"""
1. What is If Elif Else?

👉 if elif else is used when Python must check MULTIPLE conditions.

Instead of only two paths:

True
False

we can create MANY possible decision paths.

👉 Real meaning:

IF this is true
ELIF another condition is true
ELSE do something else
2. Basic syntax
if condition1:
    code

elif condition2:
    code

else:
    code
3. First basic example
a = 10

if a < 5:
    print("Low")

elif a < 15:
    print("Medium")

else:
    print("High")

👉 Output:

Medium
"""

x = 15

if x <10:
    print("False")
elif x == 15:
    print("true")
else: 
    print("check your code")


# another example # 
ab = 50.60
bc = 30.60
if ab < bc:
    print("false")
elif ab > bc:
    print("true")
else:
    print("cant check values")




