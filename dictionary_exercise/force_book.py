force_side_dict = {}
command = input()
while command != "Lumpawaroo":
    if '|' in command:
        splitted_command = command.split(' | ')
        force_side, force_user = splitted_command
        user_is_part_of_the_force = False
        for value in force_side_dict.values():
            if force_user in value:
                user_is_part_of_the_force = True
                break
        if not user_is_part_of_the_force:
            if force_side not in force_side_dict.keys():
                force_side_dict[force_side] = [force_user]
            else:
                force_side_dict[force_side].append(force_user)

    elif '->' in command:
        splitted_command = command.split(' -> ')
        force_user, force_side = splitted_command
        for key, value in force_side_dict.items():
            if force_user in value:
                force_side_dict[key].pop(value.index(force_user))
                break
        if force_side not in force_side_dict.keys():
            force_side_dict[force_side] = [force_user]
        else:
            force_side_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for force_side, force_users in force_side_dict.items():
    if len(force_users) > 0:
        print(f"Side: {force_side}, Members: {len(force_users)}")
        for user in force_users:
            print(f'! {user}')
