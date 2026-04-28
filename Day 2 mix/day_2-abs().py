#absolute value 

invoice_amount = -100
print(abs(invoice_amount))

new_invoice_amount = -20+1j
print(abs(new_invoice_amount))


invoice_amount = "100"
number =float(invoice_amount)
print(abs(number))

real = 3
expected = 4 
if abs(expected - real) > 1: 
    print("value is invalid")
else:
    print("value is valid") 

#finding the difference between two amounts with 
extracted_invoice_amount = "-100"
actual_invoice_amount = "-190"
print(abs(float(extracted_invoice_amount) - float(actual_invoice_amount)))


#if and else statements 
invoice_amount = 1000
if invoice_amount ==1000:
    print("invoice amount is valid")
else:
    print("invoice amount is invalid")


page_limitation = 100
page_scanned = 120
if page_scanned > page_limitation:
    print("page limitation is too high")

else:
    print("page limitation is valid")

#if and else statements with user input and boolean values
page_limitation = 100 
page_to_scan = int(input("enter the number of pages to scan: "))
if page_to_scan > page_limitation:
        print("page limitation is too high")
else:
        print("page limitation is valid")


#if else with user login 
user_id = "Enrique"
password = "password123"
user_id = input("enter your user id: ")
password = input("enter your password: ")
if user_id == "Enrique" and password == "password123":
    print("login successful")
else:
    print("check your username and password") 