message = input()

while True:
    command = input().split(':|:')
    current_command = command[0]
    if current_command == 'Reveal':
        print(f'You have a new text message: {message}')
        break
    elif current_command == 'InsertSpace':
        index = int(command[1])
        message = message[:index] + ' ' + message[index:]
        print(message)
    elif current_command == 'Reverse':
        substring = command[1]
        if substring in message:
            message = message.replace(substring, '', 1)
            message = message + substring[::-1]
            print(message)
        else:
            print('error')
    elif current_command == 'ChangeAll':
        substring, replacement = command[1], command[2]
        message = message.replace(substring, replacement)
        print(message)
