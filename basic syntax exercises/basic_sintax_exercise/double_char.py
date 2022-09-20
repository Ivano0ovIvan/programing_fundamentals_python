command = input()
while command != 'End':
    if command == 'SoftUni':
        continue
    for letter in range(len(command)):
        print(command[letter])
