# Whitespace cleaning #
"""
👉 Extra spaces
👉 Tabs (\t)
👉 New lines (\n)
"""
text = " Shubhankar Bisws   "
clean_data = text.strip() 
print(clean_data)

# another example # 
invoice_name = "####HI123# and ***this***"
clean_invoice = invoice_name.strip("#")
print(clean_invoice)
print(clean_invoice.strip("*"))

