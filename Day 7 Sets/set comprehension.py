"""
1. What does this mean?

👉 It means:
👉 “Creating a set dynamically using a single line of code”
2. Basic syntax
{expression for item in iterable}
3. Basic example
s = {x for x in range(5)}

print(s)
"""
a = { b for b in range(10)}
print(a)

"""x = {y for y in range(4.5)}
print(x)""" # Doesnt accept integer value# 

x = {y for y in range(9)}
print(x)

# square * exa,ple # 

z = {g * g for g in range(2)}
print(z)

# Using conditions # 
ab = {cd for cd in range(20) if cd % 2 ==0}
print(ab)