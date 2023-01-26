def password_reset_func(data):
    while True:
        current_string = input().split(' ')
        command = current_string[0]
        if command == 'Done':
            print(f"Your password is: {data}")
            break
        elif command == 'TakeOdd':
            new_data = ''
            for index, character in enumerate(data):
                if index % 2 != 0:
                    new_data += character
            data = new_data
            print(data)
        elif command == 'Cut':
            index, length = int(current_string[1]), int(current_string[2])
            data = data[:index] + data[index + length:]
            print(data)
        elif command == 'Substitute':
            substring, substitute = current_string[1], current_string[2]
            if substring in data:
                data = data.replace(substring, substitute)
                print(data)
            else:
                print("Nothing to replace!")


some_string = input()
password_reset_func(some_string)
