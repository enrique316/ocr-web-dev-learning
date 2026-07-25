# What is loop with Dict in python #
""" 
data = {
    "Name": "shubhankar",
    "age": "38",
    "city": "Rewari"
}
for key, value in data.items():
    print(key,"-", value) """ 

#another example #
""" 
captured_data = {
    "amount": 700,
    "address": "company Bash",
    "status": True
}

for key, value in captured_data.items():
    print(key, value) """ 

# OCR examples #

extracted_invoice = {
    "invoice name": "INVE234",
    "Date": "17-Jan-1923",
    "country Code": "IND-45"
}

for field, value in extracted_invoice.items():
    print(field, " : ", value)