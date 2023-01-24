number_of_characters = int(input())
counter = 0
for i in range(number_of_characters):
    letter = input()
    counter += ord(letter)
print(f"The sum equals: {counter}")