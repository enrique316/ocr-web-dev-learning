# What is nested loop # 
"""
👉 A nested loop means a loop inside another loop.

👉 The outer loop runs first.

👉 For every iteration of the outer loop, the inner loop runs completely.
"""
#Example # 
"""
for x in range(3):
    for y in range(3):
        print(x,y) """ 

# example #
for data in range(5):
    for free in range(3):
        print(data, free) 

name = ["ram","shyam"]
sections = ["A1", "B1", "C1"]
for names in name:
    for classes in sections:
        print(names, classes)

# OCR examples #

invoice = [
    ["inv123", "computer", 200]
    ['inv231', 'CPU', 700]
]
for row in invoice:
    for filed in row:
        print(filed)