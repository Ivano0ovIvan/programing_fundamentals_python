number = int(input())
wagons = [0] * number

while True:
    command = input()

    if command == 'End':
        break
    current_command = command.split(' ')
    if 'add' in current_command:
        wagons[-1] += int(current_command[-1])
    elif 'insert' in current_command:
        index = int(current_command[1])
        wagons[index] += int(current_command[-1])
    elif 'leave' in current_command:
        index = int(current_command[1])
        wagons[index] -= int(current_command[-1])
print(wagons)