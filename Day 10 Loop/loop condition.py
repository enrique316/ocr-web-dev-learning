# What is loop condition # 
""" 
A loop condition means placing an if statement inside a loop so that Python performs an action only when a condition is True.

Without a condition, the loop processes every item.

With a condition, the loop processes only the items that satisfy the condition.
"""
marks = [100, 55, 19]
names = ["Gauri", "diti", "Jaggu"]
for x,y in zip(marks, names):
    if x > 33:
        print(x,y)


# Multiple conditions #

amounts = [100000, 67000, 5000, 70000]
invoice = ["inv1", "inv2", "inv3", "inv4"]
for a,b in zip(amounts, invoice):
    if a > 5000 <70000:
        print(a, ":", b)

# OCR Example 
