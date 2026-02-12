#max() function 

invoice_amount = ["200", "500", "700"]
Convert_invoice_value= float(max(invoice_amount))
print(Convert_invoice_value) 
 

invoice_amounts = ["10", "2", "30.1"]
converted_value = [int(invoice_amount[0]), int(invoice_amount[1]), int(invoice_amount[2])]
print(max(converted_value))


invoice_company_names = ["methas", "poonias", "sharmas"]
print(max(invoice_company_names,key=len))

