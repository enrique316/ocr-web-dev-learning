"""
1. What is concatenation?
👉 Concatenation means:
👉 “Join two or more tuples into one”
"""

ab = (2, 3)
cd = (4,5)
ef = ab + cd 
print(ef)
print(ab + cd)


# with ocr example # 
invoice_data_0 = ("invoice ID", "Date")
invoice_data_1 = ("Amount", "address")
final_data = (invoice_data_0 + invoice_data_1)
print(final_data)