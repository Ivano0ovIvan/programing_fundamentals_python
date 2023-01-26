import re

data = input()
pattern = r'([\@|\#])([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})(\1)'
result = re.findall(pattern, data)
mirror_words = []
counter = 0

for pair in result:
    if pair[1] == pair[3][::-1]:
        mirror_words.append(f'{pair[1]} <=> {pair[3]}')
        counter += 1

if counter > 0:
    print(f"{counter} word pairs found!")

    if not mirror_words:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        print(', '.join(mirror_words))
else:
    print("No word pairs found!")
    print("No mirror words!")