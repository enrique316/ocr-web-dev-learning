# F string # 
"""
1. What are F Strings?

F strings mean:

👉 Inserting values directly inside a string
👉 Writing cleaner and more readable code

Instead of using .format(), values are placed inside {} directly. """

invoice_id = " GHR123"
amount = 7000 
details = f"{invoice_id} paid {amount}"
print(details)

# multiple variable # 
name = "Shubhankar"
l_name = "biswas"
address = "rewari"
age = 38
full_details = f"my name:{name} {l_name} and i live in {address} and today i will be {age} years old"
print(full_details)

# Expressions Inside F Strings #  { the integer values can be calculated inside {} }
x = 10 
y = 14
x_y = f"total is {10+14}"
print(x_y)