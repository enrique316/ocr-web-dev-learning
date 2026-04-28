invoice_value = [200, 300, 400]
total_invoice_value = sum(invoice_value)
print(total_invoice_value)

invoice_values = ["200","400","600"]
converted_invoice_values = [int(invoice_values[0]), int(invoice_values[1]), int(invoice_values[2])]
print(sum(converted_invoice_values))

extracted_invoice_values = ["20.3", "30.23", "40.2"]
converted_invoice_values = [float(extracted_invoice_values[0]), float(extracted_invoice_values[1]), float(extracted_invoice_values[2])]
print(sum(converted_invoice_values))

invoice_values = [20,30,40,50]
print(sum(invoice_values,100))

extracted_ocr = [20, 40, 50]
extra_taxes = 20
with_taxes =sum(extracted_ocr, extra_taxes)
print(with_taxes)


numbers = [0.1, 0.2]
round(sum(numbers))
print(sum([0.1, 0.2]))

