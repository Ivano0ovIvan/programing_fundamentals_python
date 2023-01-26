lst_of_characters = input().split(', ')
characters = {key: ord(key) for key in lst_of_characters}
print(characters)