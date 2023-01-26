def world_tour(destinations):
    while True:
        command = input().split(':')
        current_command = command[0]
        if current_command == 'Travel':
            print(f"Ready for world tour! Planned stops: {destinations}")
            break
        elif current_command == 'Add Stop':
            index, string = int(command[1]), command[2]
            if 0 <= index < len(destinations):
                destinations = destinations[:index] + string + destinations[index:]
        elif current_command == 'Remove Stop':
            start_index, end_index = int(command[1]), int(command[2])
            if 0 <= start_index <= end_index < len(destinations):
                destinations = destinations[:start_index] + destinations[end_index + 1:]

        elif current_command == 'Switch':
            old_sting, new_string = command[1], command[2]
            destinations = destinations.replace(old_sting, new_string)

        print(destinations)


data = input()
world_tour(data)
