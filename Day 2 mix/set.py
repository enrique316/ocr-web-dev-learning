x = set()
print(x)

invoice_numbers = ["Total", "Total", "Amount", "1900"]
find_invoice_numbers = set(invoice_numbers)
print(find_invoice_numbers)


#convert string into sets

invoice_name = "baronsbaron"
converted_invoice_name = set(invoice_name)
print(converted_invoice_name)


#convert tuple into sets

invoice_values = (10, 12, 13, 14, 10)
converted = set(invoice_values)
print(converted) 



#confidence 
invoice_data = (0.95, 0.92, 0.92, 0.93)
convert_values = set(invoice_data)
print(convert_values) 


# in set() orders are not guarantee 

new_invoice_data = 2342
converted = set(str(new_invoice_data))
print(converted)