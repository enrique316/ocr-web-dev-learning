"""
What are Complex Conditions?

👉 Complex conditions mean:

“Combining MANY conditions together to make smarter decisions”

using:

and
or
nested logic
comparison operators

inside one condition system.

Real Meaning

Earlier chapters checked:

one condition
two conditions

Now we build:

“Real decision systems”

like actual OCR and AI software.

Real OCR Scenario

Suppose invoice should be accepted only if:

confidence > 90
amount > 1000
vendor exists
invoice number exists
country is India OR USA

This is called:

Complex Validation Logic
2. First Proper Complex Example
confidence = 95
amount = 5000
vendor = "Amazon"

if confidence > 90 and amount > 1000 and vendor != "":
    print("Invoice Accepted")
else:
    print("Invoice Rejected")
"""
invoice_id = "2345IKL"
Invoice_date = "16-09-2024"
Shipping_Address = "Mumbai, India"
Amount = 100000
Paid = True
if invoice_id == "2345IKL" and Invoice_date =="16-09-2024" and Shipping_Address == "Mumbai, India" and Amount > 90000 and Paid == True:
    print("data found")
else:
    print("not found")

name = "Shubhankar"
age = 37
address = "Rewari"

if name == "Shubhankar" and age == 37 or address != "":
    print("accept")
else:
    print("reject")

# () with or and condition in complex conditions #


name1 = "Shubhankar"
last_name = "Biswas"
current_age = 36
skin_color = "fair"
if name1 == "Shubhankar" and age <=40 and ( skin_color =="fair" or skin_color == "black"):
    print("accepted")
else:
    print("not accepted")