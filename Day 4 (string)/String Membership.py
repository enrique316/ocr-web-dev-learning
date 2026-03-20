# what is String Membership # 
invoice = "myname"
print("my" in invoice)

# important things to remember that string membership is case sensetive #

my_name = "shubhankar"
print("Shubhankar" in my_name)

# Not in string memebership # 

text = " the game is on"
print("not" not in text )

# Fix case sensitivity using .lower() #

my_text = "Shubhankar"
print("shubhankar" in my_text.lower())


# OCR example # 
invoice_no = " ABP1256RahulAssociates" 
if "ABP1256" in invoice_no: 
    print("data found")
else:
    print("data invalid")

# another OCR example with .lower() scenario #
customer_name = "ABP ago petro chemicals"
if "abp" in customer_name.lower():
    print("name found")
else:
    print("name not found")