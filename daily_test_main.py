#Python practice file
#Integer operations

page_count = "5"
page_count = int(page_count)
total_pages = page_count + 10

print("Total pages:", total_pages)


# integer second example

page_count = 10

print(type(page_count)) 

#Float operations

invoice_total = "1500.75" 
invoice_total = float(invoice_total)
tax_value = 180.25
total_invoice = invoice_total + tax_value
print("Total invoice:", total_invoice)

invoice_parameter = "0.96"
print(type(invoice_parameter))

#complex type operations
invoice_value = 2+3j
print(type(invoice_value))

#string operations 
invoice_value = "₹1,500.75"
print(type(invoice_value))

#boolean operations 

x = 10
if x > 10:
    print("x is greater than 10")
else:
    print("x is not greater than 10")


invoice_value = 2000
if invoice_value > 2000:
    print("if invoice_value > 2000: dont pay")
else:
  print("if invoice_value < 2000: pay")