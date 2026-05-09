#and operator in python #
invoice_name = "rajesh"
invoice_amount = 7000

if invoice_name == 'rajesh' and invoice_amount == 7000:
 print("valid data")

# second example #

actual_amount = "7000"
extracted_amount = "8000"
if actual_amount == "7000" and extracted_amount == "8000":
 print("no amount") 

# Practice 1 # 
customer_age = 20 
if customer_age > 18 and customer_age < 60: 
 print("valid")

# Practice 2 # 
username = "admin"
password = "1234"
if username =="admin" and password =="1234":
 print("true") 

# Practice 3 # 
amount = "1200"
status = "approved"
if amount == 1200 and status == "approved":
 print("valid")

#Practice 4 #
cart_total = 1500
member = "true"
if cart_total > 1000 and member =="true":
 print("true")

# Practice 5 # 
extracted_value = "1500"
if extracted_value == int(1500):
 print("true")

ocr_value = "500"
if ocr_value .isdigit():
 convert_ocr = int( ocr_value)
 print(type(convert_ocr))

