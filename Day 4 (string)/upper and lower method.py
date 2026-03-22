# Upper and lower method in string .upper() #
name = "shubhankar"
print(name.upper())

# now .lower() #
last_name = "BISWAS"
print(last_name.lower())

# case sensitive comparison # 

my_name = "Shubhanakr Biswas"
print("Biswas" in my_name.lower())

# OCR example for .upper() and .lower() #
Invoice_name = "34#45jblassociates"
if "JBLASSOCIATES" in Invoice_name.lower():
    print("data Valid")
else:
    print("couldn't find invoice name")

# another example # 
value = "ABJ743$512jan2027"
if "abj" in value.upper():
    print("data found")
else:
    print("not found") 