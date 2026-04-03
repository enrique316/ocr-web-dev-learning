"""
1. What is Format Method?

The format method means:

👉 Inserting values into a string
👉 Creating dynamic text

Instead of joining text manually, Python replaces placeholders.

"{}".format(value) 

"""

name = "Shubhankar"
print("Hi {}".format(name))

#another example# 
my_name = "Shubhankar Biswas"
full_details = "I am {}".format(my_name)
print(full_details)

# another example # 
invoice_name = "345see"
invoice_amount = 24000
final_details = "The invoice {} amount: {}".format(invoice_name,invoice_amount)
print(final_details) 

# position based error # 
in_address = " New Delhi , India"
Date = 12-19-99
details = " The address is {0} and date is {1}".format(in_address, Date) 
print(details)

# Named Formatting (Very Important) # 

family = "wife: {wife}, husband: {husband}, kid1: {kid1}, kid2: {kid2}".format(wife =" Dimapl",husband = "Shubhankar",kid1 = "diti", kid2 = "gauri")
print(family)

