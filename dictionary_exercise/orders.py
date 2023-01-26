products = {}
command = input()
while command != 'buy':
    splitted_command = command.split(' ')
    products_name, product_price, product_quantity = splitted_command
    if products_name not in products.keys():
        products[products_name] = [float(product_price), int(product_quantity)]
    else:
        if products[products_name][0] != float(product_price):
            products[products_name][0] = float(product_price)
        products[products_name][1] += int(product_quantity)
    command = input()
for product in products.keys():
    print(f"{product} -> {(products[product][0] * products[product][1]):.2f}")
