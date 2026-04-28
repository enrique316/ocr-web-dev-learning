#not condition logic
a = 10
b = 20      
if not a > b:
    print("false")
else:
    print("true")   

invoice_amount = 1000
extracted_invoice_amount = 2000
if not invoice_amount > extracted_invoice_amount:
    print("invoice amount is valid") 


invoice_number = ""
input_invoice_number = int(input("enter the invoice number: "))
if not input_invoice_number:
    print("invoice number is empty")
else:
    print("invoice number is valid")