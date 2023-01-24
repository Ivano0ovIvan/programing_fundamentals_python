number_of_pour = int(input())
water_tank_capacity_in_lt = 255
water_counter = 0
for pours in range(number_of_pour):
    litters_of_water = int(input())
    if water_tank_capacity_in_lt - litters_of_water < 0:
        print("Insufficient capacity!")
        continue
    water_tank_capacity_in_lt -= litters_of_water
    water_counter += litters_of_water
print(water_counter)