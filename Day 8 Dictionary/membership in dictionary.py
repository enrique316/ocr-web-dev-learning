"""
1. What is membership in dictionary?

👉 Membership means:

“Checking whether something exists inside a dictionary”

👉 Usually we check:

whether a key exists
whether a required field exists
whether OCR extracted a field
2. Main operator used

We use:

in

and sometimes:

not in
3. Basic syntax
key in dictionary
"""

a = {
    'list': "done",
    'pack': "not done"

}



print('pack' in a) 

# targating the value # 
print("not done" in a.values()) 

# OCR example # 

b = {
    'invoiceID': "ID2345",
    'Invoice_Date': "03-Mar-2026",
}
print(('Invoice_Date', "03-Mar-2026") in b.items())


# another example# 

invoice = {
    'id':"FH123",
    'date': "01/01/1999",
    'paid': True
}
print(('paid', True) in invoice.items())