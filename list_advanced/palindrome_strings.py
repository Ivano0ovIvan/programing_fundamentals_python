def palindrome_filtered(word):
    if word == word[::-1]:
        return word


words = input().split(' ')
palindrome = input()
my_palinrome_list = [word for word in words if palindrome_filtered(word)]
palindrome_counter = my_palinrome_list.count(palindrome)
print(my_palinrome_list)
print(f"Found palindrome {palindrome_counter} times")
