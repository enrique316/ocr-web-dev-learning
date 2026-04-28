#min() function 
print(min(3,4,6,7,1))

invoice_value = 200
invoice_value2 = 300 
invoice_value3 = 400
invoice_value4 = 100.1 

print(min(invoice_value, invoice_value2, invoice_value3, invoice_value4))  


invoice_value = [200, 300, 400, 100.1]
print(min(invoice_value))

invoice_id = ["a", "b", "c"]
print(min(invoice_id)) 

invoice_value = [200, 300, 400, 100.1] 
least_invoice_value = min(invoice_value)
print(least_invoice_value)

invoice_values =[200, 300, 400, -100.1]
least_invoice_value = min(invoice_values)
print(least_invoice_value)

extracted_invoice_values = [-30.40, -60.1, 0.20]
smallest_extracted_invoice_value = min(extracted_invoice_values)
print(smallest_extracted_invoice_value)


extracted_invoice_values = [-30.40, 0.20, -60.1]
smallest_extracted_invoice_value = min(extracted_invoice_values)
print(smallest_extracted_invoice_value)


extracted_values =["200", "300", "400", "-100.1"]
min_extracted_value = min(extracted_values)
print(min_extracted_value)

extracted_values =["200", "300", "400", "100.1"]
min_extracted_value = float(min(extracted_values))
print(min_extracted_value)

#this is a confusion 
raw_values = ["45.5", "12.3", "abc", "9.8"]

clean_numbers = []

for v in raw_values:
    try:
        clean_numbers.append(float(v))
    except:
        pass

if clean_numbers:
    print(min(clean_numbers))


word = ["tax", "invoices", "amount"]
print(min(word, key=len)) 