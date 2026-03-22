# Counting Text in string #
name = "shubhankar"
print(name.count("a")) 

# another example #
slang = "peter parker park perter parker's car in the park" 
print(slang.count("peter")) 

# if the same text is in upper case and lower case both # 
data = " name is Shubhankar but NAME isnt sHUBHNAKAR " 
print(data.upper().count("Shubhankar"))

# another similar example # 
my_data = "Shubhankar isnt shubhankar as you think is SHUBHANKAR"
print(my_data.lower().count("shubhankar")) 

#Counting Specific Range with in string #
my_name = "shubhankar"
print(my_name.count("a",))

""" 3 different ocr examples """
text = " invoice is Invoice if Invoice"
print(text.count("Invoice"))

# second example # Detect duplicate fields # 
captured_name = " AB Jewellers AB Jewellers  AB Jewellers "
if captured_name.count("AB")>1:
 print("duplicate filed dectected ")

# Another same example #

invoice_names = " ADC Traders , ADC Traders and adc traders " 
