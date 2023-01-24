number_of_latters = int(input())
for first_letters in range(number_of_latters):
    for second_letter in range(number_of_latters):
        for third_letter in range(number_of_latters):
            print(f'{chr(97 + first_letters)}{chr(97 + second_letter)}{chr(97 + third_letter)}')
