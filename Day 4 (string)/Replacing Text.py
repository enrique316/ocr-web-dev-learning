# Replacing Text # 
name = " Subhankar"
fixed_name = name.replace("Subhankar", "Shubhankar")
print(fixed_name)

# another example # 
invoice_name = " ind3456"
fixed_invoice_name = invoice_name.replace("ind", "IND")
print(fixed_invoice_name)

# Limiting Replacement #
my_name = "SHUBHANKAR"
new_name = my_name.replace("A", "O", 1)
print(new_name)

wife_name = "DIMPAL ROY"
wife_new_name = wife_name.replace("A", "WE", 2)
print(wife_new_name)

# OCR examples #
invoice_amount = "₹500000"
print(invoice_amount.replace("₹", " "))