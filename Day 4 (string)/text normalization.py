# Text Normalization # 
"""
1. What is Text Normalization?

Text normalization means:

👉 Cleaning messy text
👉 Making text consistent

This is very important when working with OCR data.
"""

invoice = " IDG  total"
clean = invoice.strip() .lower()
print(clean)

