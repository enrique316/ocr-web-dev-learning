# String Formatting #
"""
2. Key Concept

Python provides multiple ways:

f-strings (modern and recommended)
.format) method
% formatting (older method)
it Works with int, float, etc. 
"""
# example using 'f' insert #
invoice_name = "ABJ Associates"
Invoice_amount = 8000
print(f"The {invoice_name} and the pending amount is {Invoice_amount}")

# example using .format insert # 
raw_invoice_n = "JDC industries " 
pending_amount = 5670
print("The company name is {} and pending amount is {}".format(raw_invoice_n,pending_amount)) 

# another same example #
my_name = "Shhankar"
Age = 37
Address = "Company Bagh, Rewari, Haryana" 
full_details = "my name is {} and I was born on {} and i am from {}".format(my_name,Age, Address) 
print(full_details)

# Using % method # 

print("my %s and my bod %dand my address" % (my_name, Age)) 

# formatting numbers #
number = 3545.7 
print(f"{number:.2f}")
