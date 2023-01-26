raw_activation_key = input()
activation_key = ''
start_index = 0
end_index = 0
while True:
    current_string = input().split('>>>')
    command = current_string[0]
    if command == 'Generate':
        activation_key = raw_activation_key
        print(f"Your activation key is: {activation_key}")
        break
    elif command == 'Contains':
        substring = current_string[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command == 'Flip':
        case = current_string[1]
        start_index = int(current_string[2])
        end_index = int(current_string[3])
        if case == 'Upper':
            new_string = raw_activation_key[start_index:end_index]
            new_string = new_string.upper()
            raw_activation_key = raw_activation_key[:start_index] + new_string + raw_activation_key[end_index:]
            print(raw_activation_key)
        elif case == 'Lower':
            new_string = raw_activation_key[start_index:end_index]
            new_string = new_string.lower()
            raw_activation_key = raw_activation_key[:start_index] + new_string + raw_activation_key[end_index:]
            print(raw_activation_key)
    elif command == 'Slice':
        start_index = int(current_string[1])
        end_index = int(current_string[2])
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)