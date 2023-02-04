def decipher_func(secret_word):
    new_word = []
    num = []
    characters = []
    for i in secret_word:
        if i.isdigit():
            num.append(i)
    num = ''.join(num)
    num_as_char = chr(int(num))
    new_word.append(num_as_char)
    for char in secret_word:
        if char.isalpha():
            characters.append(char)
    characters[0], characters[-1] = characters[-1], characters[0]
    characters = ''.join(characters)
    new_word.append(characters)
    new_word = ''.join(new_word)
    return new_word


secret_message = input().split(' ')
deciphered_message = []
for word in secret_message:
    result = decipher_func(word)
    deciphered_message.append(result)
print(' '.join(deciphered_message))