first_string = input()
second_string = input()
last_printed_string = first_string
for character in range(len(first_string)):
    left_part = second_string[: character + 1]
    right_part = first_string[character + 1:]
    current_string = left_part + right_part
    if current_string == last_printed_string:
        continue
    print(current_string)
    last_printed_string = current_string
