"""
1. What is Else with Loop?

👉 Most beginners know that else is used with an if statement.

Example:

age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")

But Python also allows us to use else with loops.

Both for and while loops support an else block.

Real Meaning

Think of a teacher checking attendance.

The teacher starts checking every student's name.

If the teacher checks every student without interruption, they finally say:

Attendance Completed

This is exactly how else works with a loop.

The else block runs only after the loop finishes all of its iterations successfully.

However, if someone interrupts the teacher before finishing, the teacher never says:

Attendance Completed

The same thing happens when Python encounters a break.

First Example
for i in range(3):
    print(i)
else:
    print("Done")
Output
0
1
2
Done

Notice that "Done" is printed only after the loop has printed all the numbers.

"""
""" for x in range(3):
    print(x)
else:
    print("done")

for a in range (10):
    print(a) 
else:
    print("checked") 

#example#
for xz in range(10):
    print(xz)"""

for x in range(7):
 if x ==3:
    break
 print(x)
else:
    ("done")

for z in range(10):
 if z ==1:
   break
 print(z)
else:
  ("let me check")

#OCR Example # 
extracted_feilds ={
  "name":"Shubhankar",
  "last name": "Biswas",
  "address": "rewari",
}
for extracted_feilds in extracted_feilds:
  print(extracted_feilds)
else:
  print("done")

