"""
1. What are Multiple Conditions?

👉 Multiple conditions mean:

“Checking many conditions together inside one decision”

using:

and
or
"""

last_fetch_amount = 40000
today_fetch_amount = 10000
if last_fetch_amount >1000 and today_fetch_amount > 5000:
    print("amount approved")
else:
    print("amount not approved")


# another example # 

confidence_level = 90
captured_amount = 50000
invoice_no = "inv1234"
if confidence_level > 80 and confidence_level <90  and invoice_no !="":
 print("ture")
else:
   print("false")


# example # 
