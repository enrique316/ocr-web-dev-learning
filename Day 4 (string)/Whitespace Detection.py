#Whitespace Detection#
text = " "
print(text.isspace())

"""
Reads each character in the string
Checks if it is a whitespace character
Includes:
space " "
tab \t
newline \n
"""
ab = "\t\t"
print(ab.isspace())

#___# 
ac = "\n"
print(ac.isspace())

# OCR examples #

data = " "
if data.strip() == "":
    print("data valid")
else:
    print("data invalid")

# more examples # 

