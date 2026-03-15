# string #
name = "shubhankar"
print(name)
print(type(name))

# three different types of quotes for string #
# single '' quote # 

invoice_name = 'ABD group'
print(type(invoice_name))

# double quote "" 
update_invoice = "xyzgroup"
print(type(update_invoice))

# triple quote ''''' # 
document = """Invoice Number: 123
Total: 1200
Date: 2025""" 
print(document)

x = """drc
name: DSC group
Address: Zuric"""
print(x)


# len() chapter 3 # 

company_name = """Rohde Motorcycle company"""
Address = """ 340/5 Jack's street
City: Florida
Country: USA
"""
print(len(company_name))
print(company_name, Address, sep=',')