"""
What is String Formatting?

String formatting means:

👉 Combining variables (data) with text
👉 Creating readable output from data

"""

invoice_name = "bridge communications"
invoice_amount = 7000
print(invoice_name + " paid " + str(invoice_amount))

# another example # 
amount = 5000
name = "abc" 
output = str(amount) + " is given by " + name 
print(output)

# OCR examples # 

invoice_name_1 = " Maruti Industries"
invoice_amount = 3450.1 
address = " Mumbai, MH, India"
print(invoice_name_1 + " paid amount : " + str(invoice_amount) + " In " + address )