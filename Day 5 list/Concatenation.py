# Concatenation in list # 
"""
1. What is Concatenation?
👉 Concatenation means joining two or more lists together
👉 It creates a new combined list
"""

a = [1,2,3,4]
b = [4,3,2,1]
print( a + b)

# Example with mixed data types # 

invoice_details = ["Name", "Address", "12/01/1987"]
amounts = [23400, 3500, 123.4]
complete_details = invoice_details + amounts
print("Merchant details:", complete_details)