def palindrome(digits):
    for current_number in digits:
        if current_number == current_number[:: -1]:
            print('True')
        else:
            print('False')


numbers = input()
numbers_as_int = numbers.split(', ')
is_palindrome = palindrome(numbers_as_int)
