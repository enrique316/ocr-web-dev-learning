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