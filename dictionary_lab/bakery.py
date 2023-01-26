items = input().split()
bakery = {}
for index in range(0, len(items), 2):
    key = items[index]
    value = items[index + 1]
    bakery[key] = int(value)
print(bakery)
