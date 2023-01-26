contests = {}
users = {}
users_points = {}
while True:
    command = input().split(':')
    if command[0] == 'end of contests':
        break
    contest, password_for_contest = command[0], command[1]
    if contest not in contests.keys():
        contests[contest] = [password_for_contest]

while True:
    current_command = input().split('=>')
    if current_command[0] == 'end of submissions':
        break
    current_contest, password, username, points = current_command[0], current_command[1], current_command[2], int(current_command[3])
    if current_contest in contests.keys() and password == contests[current_contest][0]:
        if username not in users.keys():
            users[username] = {current_contest: points}
            users_points[username] = [points]
        else:
            if users[username].keys() == current_contest and users[username][current_contest][0] < points:
                users[username][current_contest][0] = [points]
                users_points[username][0] -= users[username][current_contest][0]
                users_points[username][0] += points
            elif users[username].keys() == current_contest and users[username][current_contest][0] >= points:
                break
            else:
                users[username][current_contest] = [points]
                users_points[username][0] += points
print(users)
print(users_points)