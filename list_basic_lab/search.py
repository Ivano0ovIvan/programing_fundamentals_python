nuber_of_strings = int(input())
code_word = input()
lst_of_strings = []
lst_of_strings_filtered = []
for i in range(nuber_of_strings):
    current_string = input()
    lst_of_strings.append(current_string)
    current_string_splited = current_string.split(' ')
    if code_word in current_string_splited:
        lst_of_strings_filtered.append(current_string)
print(lst_of_strings)
print(lst_of_strings_filtered)