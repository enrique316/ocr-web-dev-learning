invoice_number = 100
print(isinstance(invoice_number, int))

invoice_amount =input("enter amount:")
print(isinstance(invoice_amount, int))
print(isinstance(invoice_amount, float))
print(isinstance(invoice_amount, str))


#check list# 
invoice_amounts = [1,2,3]
print(isinstance(invoice_amounts, list))
print(isinstance(invoice_amounts, tuple))
print(isinstance(invoice_amounts, set)) 

invoice_amounts = {1,2,3}
print(isinstance(invoice_amounts, list))
print(isinstance(invoice_amounts, tuple))
print(isinstance(invoice_amounts, set)) 

#check multiple values using isinstance# 
invoice_number = 10
print(isinstance(invoice_number, (int, float))) 


ocr_output = ["Total", "4500"]
ocr_output = {"total": "4500"}


if isinstance(ocr_output, list):
    print("Process as token list")

if isinstance(ocr_output, dict):
    print("Process as structured data")

extracted_data = ["Total", "4500"]
extracted_data = {"total": "4500"}

if isinstance(extracted_data, list):
    print("valid")
if isinstance(extracted_data, dict):
    print("invalid")
