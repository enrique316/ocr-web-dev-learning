name = "Shubhankar", "Biswas"
full_name = " ".join(name)
print(full_name)

# another example  #
name_1 = "Diti" , "Biswas"
full_name_1 = " ".join(name_1)
print(full_name_1)

# joining other symbols - : * # 

items = "Alpha", "beta", "Charlie"
combined = ":".join(items)
print(combined)

""" all the values must be in string format """
#but lets try with single quotes '' #
value = 'Hi', 'I', 'am', 'John'
x = ' '.join(value)
print(x)
# this works# 

# what if the value is integer # 
numbers = [1,2,3,4]
combined_numbers = " ".join(map(str, numbers))
print(combined_numbers) 


# OCR examples #

invoice_values = [200, 500, 700]
filterd_invoice_data = ":".join(map(str, invoice_values))
print(filterd_invoice_data) 

# beginner friendly approach# 
invoice_values = [200, 500, 700]
filterd_invoice_data = [str(n) for n in invoice_values]
print(" ".join(filterd_invoice_data))
