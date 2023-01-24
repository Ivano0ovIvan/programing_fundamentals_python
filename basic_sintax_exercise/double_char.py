command = input()
word = ''
while command != 'End':
    if command != 'SoftUni':
        for char in command:
            print(char * 2, end = '')
        print()
    command = input()
