first_sequence = input().split(', ')
second_sequence = input().split(', ')
substrings = []
for firs_word in first_sequence:
    for second_word in second_sequence:
        if firs_word in second_word:
            substrings.append(firs_word)
            break
print(substrings)