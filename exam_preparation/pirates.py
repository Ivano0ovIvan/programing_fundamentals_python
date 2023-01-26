def print_function(cities):
    if cities:
        print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
        for city in cities:
            print(f"{city} -> Population: {cities[city][0]} citizens, Gold: {cities[city][1]} kg")
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


def prosper_function(town, gold_added, cities):
    if gold_added > 0:
        cities[town][1] += gold_added
        print(f"{gold_added} gold added to the city treasury. {town} now has {cities[town][1]} gold.")
    else:
        print("Gold added cannot be a negative number!")


def plunder_function(town, people, stolen_gold, cities):
    if town in cities.keys():
        print(f"{town} plundered! {stolen_gold} gold stolen, {people} citizens killed.")
        cities[town][0] -= people
        cities[town][1] -= stolen_gold
        if cities[town][0] <= 0 or cities[town][1] <= 0:
            print(f"{town} has been wiped off the map!")
            del cities[town]


cities = {}
while True:
    command = input().split('||')
    if command[0] == 'Sail':
        break
    city, population, gold = command[0], int(command[1]), int(command[2])
    if city not in cities:
        cities[city] = [population, gold]
    else:
        cities[city][0] += population
        cities[city][1] += gold

while True:
    command = input().split('=>')
    if command[0] == 'End':
        print_function(cities)
        break
    town = command[1]
    if command[0] == 'Plunder':
        people = int(command[2])
        stolen_gold = int(command[3])
        plunder_function(town, people, stolen_gold, cities)
    elif command[0] == 'Prosper':
        gold_added = int(command[2])
        prosper_function(town, gold_added, cities)
