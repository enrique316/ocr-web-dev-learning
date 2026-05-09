# not operator # 
extract_data = 10
print(not 10 <2)

# user login example # 
account_logged_in = True
print( not account_logged_in)

# Important Python Behavior #
"""not works on truthy and falsy values.
Values Python treats as False """
"""
0
""
[]
None
False
"""
user_name = ""
print(not user_name)

# OCR scenario example #
reference_no = ""
if not reference_no: 
    print("reference no not detected")

# Example #
user_id = "rambo@1234*#"
if not user_id:
    print("invalid user")
else:
    print("account login successful")

""" 🧪 5 Practice Mini Chapters"""
"""Run these and send me your answers.
Practice 1: Login Check
logged_in = False
Print if the user is not logged in."""
logged_in = False
if not logged_in:
    print("not logged in")
else: 
    print("logged in")


"""Practice 2: Document Validation
document_text = ""
Check if the document has no text."""
document_text = ""
if not document_text:
    print("has no text")
else:
    print("has text")
"""Practice 3: Payment Status
paid = True
Print if the invoice is not paid."""
paid = True
if not paid:
    print("not paid")
else: 
    print("already paid")
"""Practice 4: OCR Field Check
invoice_number = ""
Check if invoice number is missing."""
invoice_number = ""
if not invoice_number:
    print("invoice number missing")
else:
    print("invoice no present")
"""Practice 5: Inventory System
stock = 0
Check if the item is not available in stock."""
stock = 0
if not stock:
    print("stock has no items")
else:
    print("stock has itmes")