def encrypting_function(secret_message):

    while True:
        command = input().split('|')
        if command[0] == 'Decode':
            print(f"The decrypted message is: {secret_message}")
            break
        elif command[0] == 'Move':
            number_of_letters_to_move = int(command[1])
            secret_message = secret_message[number_of_letters_to_move:] + secret_message[0:number_of_letters_to_move]
        elif command[0] == 'Insert':
            index, value = int(command[1]), command[2]
            secret_message = secret_message[:index] + value + secret_message[index:]
        elif command[0] == 'ChangeAll':
            substring, replacement = command[1], command[2]
            secret_message = secret_message.replace(substring, replacement)


encrypted_message = input()
encrypting_function(encrypted_message)
