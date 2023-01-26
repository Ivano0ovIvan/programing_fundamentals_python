students = {}
languages = {}
command = input()

while command != "exam finished":
    if 'banned' in command:
        banned_username, status = command.split('-')
        if banned_username in students.keys():
            del students[banned_username]
    else:
        username, language, points = command.split('-')
        if language not in languages:
            languages[language] = 1
        else:
            languages[language] += 1
        if username not in students.keys():
            students[username] = [language, int(points)]
        else:
            if students[username][0] == language and students[username][1] < int(points):
                students[username][1] = int(points)
    command = input()
print('Results:')
for user, point in students.items():
    print(f'{user} | {int(students[user][1])}')
print('Submissions:')
for lang, count in languages.items():
    print(f'{lang} - {languages[lang]}')