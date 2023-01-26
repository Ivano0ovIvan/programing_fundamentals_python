number_of_lines = int(input())
for i in range(number_of_lines):
    text = input()
    new_text = ''
    for i, v in enumerate(text):
        if v == '@':
            start_index_1 = i
        if v == '|':
            end_index_1 = i
        if v == '#':
            start_index_2 = i
        if v == '*':
            end_index_2 = i
    name = text[start_index_1 + 1:end_index_1]
    age = text[start_index_2 + 1:end_index_2]
    print(f"{name} is {age} years old.")