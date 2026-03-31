# Digit validation # 
invoice_number = "123456"
print(invoice_number.isdigit())

# another example #
invoice_2 = "IND2345"
print(invoice_2.isdigit())

#  OCR example - Example 3: Safe Data Processing #

ab = "50000"
if ab.isdigit():
 new_value = int(ab)
 print(new_value)