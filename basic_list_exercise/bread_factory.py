events = input().split('|')
total_coins = 100
total_energy = 100
factory_is_open = True
for event in events:
    event_items = event.split('-')
    event_type = event_items[0]
    event_value = int(event_items[1])
    if event_type == 'rest':
        curren_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - curren_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif event_type == 'order':
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            print("You had to rest!")
            total_energy += 50
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {event_type}.")
        else:
            print("Closed! Cannot afford {ingredient}." )
            factory_is_open = False
            break
if factory_is_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
