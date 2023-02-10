def family_car_tax_calculator(km, years):
    discounts = years * 5
    raises = (km // 3000) * 12
    current_tax = family_car_initial_tax - discounts + raises
    return current_tax

def heavy_duty_car_tax_calculator(km, years):
    discounts = years * 8
    raises = (km // 9000) * 14
    current_tax = heavy_duty_car_initial_tax - discounts + raises
    return current_tax

def sports_car_tax_calculator(km, years):
    discounts = years * 9
    raises = (km // 2000) * 18
    current_tax = sports_car_initial_tax - discounts + raises
    return current_tax


vehicles = input().split('>>')
family_car_initial_tax = 50
heavy_duty_car_initial_tax = 80
sports_car_initial_tax = 100
current_tax = 0
index = 0
total_taxes = 0
for vehicle in range(len(vehicles)):
    current_vehicle = vehicles[index].split(' ')
    type_of_vehicle = current_vehicle[0]
    years_of_vehicle = int(current_vehicle[1])
    kilometers = int(current_vehicle[2])
    if type_of_vehicle == 'family':
        tax_to_pay = family_car_tax_calculator(kilometers, years_of_vehicle)
        total_taxes += tax_to_pay
        print(f'A {type_of_vehicle} car will pay {tax_to_pay:.2f} euros in taxes.')
    elif type_of_vehicle == 'heavyDuty':
        tax_to_pay = heavy_duty_car_tax_calculator(kilometers, years_of_vehicle)
        total_taxes += tax_to_pay
        print(f'A {type_of_vehicle} car will pay {tax_to_pay:.2f} euros in taxes.')
    elif type_of_vehicle == 'sports':
        tax_to_pay = sports_car_tax_calculator(kilometers, years_of_vehicle)
        total_taxes += tax_to_pay
        print(f'A {type_of_vehicle} car will pay {tax_to_pay:.2f} euros in taxes.')
    else:
        print(f'Invalid car type.')
        index += 1
        continue
    index += 1
print(f'The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.')