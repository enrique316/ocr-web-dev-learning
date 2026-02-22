print(str(10))
print(float(20))
print(int(40))


#types built in functions (type)
x = 10
print(type(x))

invoice_value = 3000.76
print(type(invoice_value))

invoice_name = "Invoice 001"
print(type(invoice_name))

#(len) built in function
invoice_name = "Invoice 001"
print(len(invoice_name))

vendor_name = "ABC Corporation"
print(len(vendor_name))

pages = [1,2,3,4,5]
print(len(pages))

pages_types = {1,2,3,4,5}
print(len(pages_types)) 

#int() built in types 
print(int(5)) 

#str() built in function 
print(str("10 byters"))

#float() built in function 
print(float(20))


#bool() built in function 
invoice = input("bill of lading")
if bool(invoice): 
    print("bill of lading is valid")
else:
    print("invoice is not valid") 

invice_value = 700
if bool(invice_value >1000):
    print("invoice value is valid")
else:
    print("not valid")

invoice_name = "invoice_009"
if bool(invoice_name == "invoice_007"):
    print("invoice name is valid")
else:    print("invoice name is not valid")

#bool() built in function with date
invoice_date ="Jan-01-2024"
if bool(invoice_date == "Jan-01-2026"):
    print("invoice date is valid")
else:
    print("invoice date is wrong")

gst_number = ""
if bool(gst_number):
    print("gst number is found")
else:
    print("gst number is not found")

    #()boolean page no 

    page_numbers = ["page1", "page2", "page3", "page4", "page5", "page6", "page7", "page8", "page9", "page10", "page11"]
    if bool("page12" in page_numbers):
        print("page numbers are valid")
    else:
        print("page numbers are not valid")


api_key = ""
if(bool(api_key == "12345")):
    print("api key accepted")
else:
    print("api key not accepted") 


 #abs() built in function 
    expected_amount = 5000
    actual_amount = -7000
    print(abs(expected_amount - actual_amount))




#abs() confidence deviation in ocr environment 
invoice_amount = 1000
extracted_amount_from_invoice = 1200
print(abs(invoice_amount - extracted_amount_from_invoice))   

difference = abs(invoice_amount - extracted_amount_from_invoice)
if difference >= 200:
    print("amount deviation is acceptable")
else:    
    print("amount deviation is not acceptable") 


#abs() distance or change tracking in logistics
initial_distance = 100
final_distance = 150 
difference = abs(final_distance - initial_distance)
if difference >= 100:
    print("distance change is significant")
else:
    print("distance change is not significant")


total_weight_invoice = 500
extracted_weight_invoice = 550 
difference = abs(extracted_weight_invoice - total_weight_invoice)
if difference <= 50:
    print("weight deviation is acceptable")
else:
    print("weight deviation is not acceptable")

#input() built in function
input("Enter your name: ")


#help() built in function
help(input)

#input() built in function with validation

user_input_value = input("enter an invoice page number: ")
if user_input_value.isdigit():
    print(f"Valid page number entered: {user_input_value}")
else:
    print("Invalid page number. Please enter a numeric value.")