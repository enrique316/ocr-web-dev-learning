# Else with loop # 
"""
👉 In Python, a loop can have an else block.

👉 The else block runs after the loop finishes normally.

👉 If the loop is stopped using break, the else block does not run.
"""
"""
for x in range(5):
   print(x)
else:
   print("hi")

# another example #

for a in range(7):
   print(a)
else:
   print("bye") """ 

# another example # 
for d in range(10):
   if d == 1:
      break
   print(d)
else:
   print("hehe")

# OCR Example # 
extract_data = [
   "Name", 
    "Address",
    "amount",
    "City"
]
for a in extract_data:
   if a == "amount":
      print(a)
else:
      print("checked")