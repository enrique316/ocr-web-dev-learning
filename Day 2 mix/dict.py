#dict() dictionary variable 

extract_data = dict(
    invoice_number = 3459,
    total_amount_value = 4700,
    gts="12%"
)
print(extract_data)


invoice_details = dict(
    invoice_date = "12Jan1989", 
    total_extracted_amount = "₹5000",
    gts = "none",
)
print(invoice_details)


values = [("invoice_number", 567), ("invoice_amount", 4000)]
invoice_details1 = dict(values)
print(invoice_details1) 


#dictionary using curly braces# 

invoice = {
    "invoice_number": 7800, 
    "invoice_date": 12/17/19, 
}

print(invoice)


invoice_details = {
    "invoice_number": 700, 
    "invoice_date": 900,
}

#accessing values# 

invoice_details = {
    "invoice_number": 700, 
    "invoice_date": 30,
}
print(invoice_details["invoice_number"])



invoice = dict(
    invoice_number = 3459,
    total_amount_value = 4700,
    gts="12%"   
)
print(invoice[("invoice_number")])


#list vs dictionary#
