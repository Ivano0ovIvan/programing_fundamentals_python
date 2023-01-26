import re

text = input()
pattern = r'([\@|\#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'
matches = re.findall(pattern, text)
mirror_word = []
if matches:
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")
for pair in matches:
    if pair[1] == pair[2][::-1]:
        mirror_word.append(f'{pair[1]} <=> {pair[2]}')
if not mirror_word:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(', '.join(mirror_word))
