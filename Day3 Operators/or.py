# or operator in python #

user_age = 18
account_activated = True

if user_age <= 18 or account_activated:
    print("user is valid")

#another example # 
extracted_value = 700
if extracted_value <0 or extracted_value > 600:
    print("value accepted")
else:
    print("value not accepted")

# example with login system # 
user_name = "diti"
password = "rambo123"

if user_name or password:
    print("user valid")
else:
    print("user not valid")

# combining or and and operator together #
use_age = 21 
user_country = "india"
if user_age > 18 and (user_country == "india" or user_country == "USA"):
    print("user valid")
else:
    print("user invalid")

# 5 practice #
"""Practice 1: Age Eligibility
Create
age = 16
Check if age is less than 18 OR greater than 60. """

age = 16
if age <18 or age > 60:
    print("true")


"""Practice 2: Login Access
username = "user"
backup_user = "admin"
Check if username is "admin" OR backup_user is "admin". """

user_name = "user"
backup_user = "admin"
if user_name == "admin" or backup_user == "admin":
    print("user name is admin")

"""Practice 3: Temperature Alert
temperature = 42
Check if temperature is greater than 40 OR less than 5."""

temperature = 42
if temperature > 40 or temperature < 5 :
    print("true")
else:
    print("false")

"""Practice 4: OCR Document Check
invoice_number = ""
reference_number = "REF778" """
"""Check if invoice_number OR reference_number exists."""
invoice_number = ""
reference_number = "REF778" 
if invoice_number == "" or reference_number == "REF778":
  print("valid")
else:
    print("invalid")

"""Practice 5: Payment System
upi = ""
card = "available"
Check if upi OR card is available."""

upi = ""
card = "available"
if upi or card:
    print("valid")
else:
    print("invalid")
