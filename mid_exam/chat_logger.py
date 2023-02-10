def chat_func(comm):
    if comm == 'Chat':
        chat_history.append(command[1])
    elif comm == 'Delete':
        if command[1] in chat_history:
            chat_history.remove(command[1])
    elif comm == 'Edit':
        if command[1] in chat_history:
            message_index = chat_history.index(command[1])
            chat_history.remove(command[1])
            chat_history.insert(message_index, command[2])
    elif comm == 'Pin':
        if command[1] in chat_history:
            message_index = chat_history.index(command[1])
            pin_message = chat_history.pop(message_index)
            chat_history.append(pin_message)
    elif comm == 'Spam':
        for message in command:
            if message != comm:
                chat_history.append(message)
    return chat_history

chat_history = []
while True:
    command = input().split(' ')
    data = command[0]
    if data == 'end':
        break
    else:
        chat_func(data)

[print(i) for i in chat_history]
