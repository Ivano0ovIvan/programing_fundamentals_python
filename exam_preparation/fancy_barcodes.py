import re

pattern = r'\@[\#]+([A-z][A-Za-z0-9]{4,}[A-Z])\@[\#]+'
number_of_barcodes = int(input())
for i in range(number_of_barcodes):
    data = input()
    current_match = re.findall(pattern, data)
    if current_match:
        product_group = []
        for char in current_match[0]:
            if char.isdigit():
                product_group.append(char)
        if product_group:
            print(f"Product group: {''.join(product_group)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
