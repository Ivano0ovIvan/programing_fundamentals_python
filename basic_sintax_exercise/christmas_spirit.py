quantity_of_decoration = int(input())
days_left = int(input())
total_budget = 0
total_spirit = 0
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
ornament_set_spirit = 5
tree_skirt_spirit = 3
tree_garland_spirit = 10
tree_lights_spirit = 17
for current_day in range(1, days_left + 1):
    if current_day % 11 == 0:
        quantity_of_decoration += 2
    if current_day % 2 == 0:
        total_budget += ornament_set_price * quantity_of_decoration
        total_spirit += ornament_set_spirit
    if current_day % 3 == 0:
        total_budget += (tree_skirt_price + tree_garland_price) * quantity_of_decoration
        total_spirit += (tree_skirt_spirit + tree_garland_spirit)
    if current_day % 5 == 0:
        total_budget += tree_lights_price * quantity_of_decoration
        total_spirit += tree_lights_spirit
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        total_budget += tree_skirt_price + tree_garland_price + tree_lights_price
if days_left % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_budget}")
print(f"Total spirit: {total_spirit}")