"""
1. What are Logical Operators?

👉 Logical operators are used to combine multiple conditions.

They help Python answer questions like:

Is condition A true AND condition B true?

or

Is at least one condition true?

👉 Python mainly uses 3 logical operators:

Operator	Meaning
and	Both conditions must be True
or	At least one condition must be True
not	Reverses True/False
2. First basic example
print(True and False)

👉 Output:

False
Why?

Because:

True AND False

means BOTH must be True.

But one condition is False.

So final result becomes:

False
3. Understanding and

👉 and only returns True when BOTH conditions are True.

Visual Table
Condition A	Condition B	Result
True	True	True
True	False	False
False	True	False
False	False	False
Example 1
print(10 > 5 and 20 > 10)
"""
a = 10
b = 7 
c = 2 
if a > b and c < b :
    print("true")
else:
    print("false")

User_name = "lobby123#123"
password = "sadasdasi@343545@"
if User_name == "lobby123#123" and password == "sadasdasi@343545@":
    print("user authenticate")
else:
    print("check credentials") 

# now one true and one false condition # 
"""
login_id = input()
login_password = input()
if login_id == "JalebeeBai123" and login_password == "SDDRRsdsewe!@#%$#@":
    print("user authenticated")
else:
    print("invalid user")"""

product_weight = 100

if product_weight > 90 < 80 :
    print('true')
else:
    print('false')