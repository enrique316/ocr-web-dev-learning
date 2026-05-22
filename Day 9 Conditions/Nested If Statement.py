"""
What is Nested If?

👉 Nested if means:

“An if statement inside another if statement”

Real meaning:

First condition must pass
THEN second condition is checked
Why Nested If is Used?

Nested if is used when:

👉 one condition depends on another condition.

Real World Example

Suppose an OCR system should:

Step 1:

Check OCR confidence

Only if confidence is valid:

Step 2:

Check invoice amount

This is called dependent checking.

2. Basic Syntax
if condition1:

    if condition2:
        code
Important understanding

The second if only runs if first if becomes True.

3. First Proper Example
a = 10

if a > 5:

    if a < 20:
        print("OK")
"""
extracted_amount = 34567

if extracted_amount > 30000:
    if extracted_amount < 35000:
        print("data valid")
    else:
        print("data not valid")


# another example # 


print(2>5<1)

# example #

"""user_login = True
amount_fetech_request = int(input())
if user_login: 
    if amount_fetech_request > 0 and amount_fetech_request <5000:
        print("withdraw amount")
    else:
        print("invalid amount")"""
#Nested If With Else#

captured_amount = 10000
if captured_amount > 11000:

    if captured_amount < 5000:
     print("amount valid")
    else:
        print("amount not valid")
else:
    print("check value again")

# Age verification example # 

age = int(input())
if age > 18:
    if age < 61:
        print("Age verified")
    else:
        print("invalid age")
else:
    print("type your age again")