"""
1. What does this mean?

👉 It means:

👉 “Accessing set items one by one using a loop”

2. Why looping is needed

👉 Sets do NOT support indexing

❌ This does not work:

s = {1, 2, 3}

print(s[0])

👉 Error

👉 So we use loops to access values
"""

a = {1,2,3}
for b in a:
    print(b)

#OCR examples # 
name = {"Shubhankar", "Dimpal", "Diti", "Gauri"}
for family in name:
    print(family)