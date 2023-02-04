def price_calculator(type_of_product, number_of_products):
    total_price = 0
    if type_of_product == "coffee":
        total_price = number_of_products * 1.50
    elif type_of_product == 'coke':
        total_price = number_of_products * 1.40
    elif type_of_product == 'water':
        total_price = number_of_products * 1.00
    elif type_of_product == "snacks":
        total_price = number_of_products * 2.00
    return total_price


product = input()
product_quantity = int(input())
print(f'{price_calculator(product, product_quantity):.2f}')
