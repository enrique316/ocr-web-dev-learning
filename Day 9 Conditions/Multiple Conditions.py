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


# a