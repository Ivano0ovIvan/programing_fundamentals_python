def print_function(data):
    result = ''
    for current_car in data:
        mileage = data[current_car][0]
        fuel = data[current_car][1]
        result += f"{current_car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.\n"
    return result


def revert_func(car, kilometers, data):
    data[car][0] -= kilometers
    if data[car][0] >= 10000:
        print(f"{car} mileage decreased by {kilometers} kilometers")
    else:
        data[car][0] = 10000


def refuel_func(car, fresh_fuel, data):
    need_fuel = 75 - data[car][1]
    if fresh_fuel <= need_fuel:
        data[car][1] += fresh_fuel
        print(f"{car} refueled with {fresh_fuel} liters")
    else:
        data[car][1] = 75
        print(f"{car} refueled with {need_fuel} liters")


def drive_func(car, distance, needed_fuel, data):
    if data[car][1] < needed_fuel:
        print("Not enough fuel to make that ride")
    else:
        data[car][0] += distance
        data[car][1] -= needed_fuel
        print(f"{car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")
        if data[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            del data[car]


def store_data_func(number):
    data = {}
    for _ in range(number):
        car, millage, fuel = input().split('|')
        data[car] = [int(millage), int(fuel)]
    return data


def need_for_speed_func(number):
    data = store_data_func(number)

    while True:
        commands = input().split(' : ')
        if commands[0] == 'Stop':
            print(print_function(data))
            break
        command = commands[0]
        car = commands[1]
        if command == 'Drive':
            distance, needed_fuel = int(commands[2]), int(commands[3])
            drive_func(car, distance, needed_fuel, data)
        elif command == 'Refuel':
            fresh_fuel = int(commands[2])
            refuel_func(car, fresh_fuel, data)
        elif command == 'Revert':
            kilometers = int(commands[2])
            revert_func(car, kilometers, data)


number_of_cars = int(input())
need_for_speed_func(number_of_cars)
