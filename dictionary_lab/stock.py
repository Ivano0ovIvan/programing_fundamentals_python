items = input().split()
searched_items = input().split()
bakery = {}
for index in range(0, len(items), 2):
    key = items[index]
    value = items[index + 1]
    bakery[key] = int(value)
for product in searched_items:
    if product in bakery.keys():
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
