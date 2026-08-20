# What is default parameters in python #
""" A Default Parameter is a parameter that already has a value assigned to it when the function is created."""
def greet(name= 'Shubhankar'):
    print("Hello:", name)
greet()

# Another example #
def user(loginID = "Bossman1234"):
    print("User verified by :", loginID)
user()

# This is another example where we dont provide parameter value #
"""
def greet(name=user):
    print("Hello:", user)

greet("Shubhankar")
# Another example #
def check(amount=any):
    print("Captured_amount:", amount)
check(5000)""" 

# example #
def capture(amount=any, date=any, name="user"):
    print("finale Amount:",amount, "extraction_date:",date, "user_name:",name)
capture(7000, "12-10-1988", "rajeev")
