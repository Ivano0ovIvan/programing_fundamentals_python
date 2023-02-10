def length_is_valid(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def characters_validation(name):
    for character in name:
        if not (character.isalnum() or character == '_' or character == '-'):
            return False
    return True


def no_reduntnant(name):
    if ' ' in name:
        return False
    return True


def username_validation(name):
    if length_is_valid(name) and characters_validation(name) and no_reduntnant(name):
        return True
    return False


usernames = input().split(', ')
for username in usernames:
    if username_validation(username):
        print(username)
