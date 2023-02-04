def shell_filler(number_of_the_shell):
    return 2 * (number_of_the_shell ** 2)


number_of_electrons = int(input())
electrons_counter = number_of_electrons
shell_counter = 1
filled_shells = []
current_electrons = 0
for electrons in range(1,number_of_electrons + 1):
    if electrons_counter > shell_filler(shell_counter):
        current_electrons += 1
        if current_electrons == shell_filler(shell_counter):
            filled_shells.append(current_electrons)
            shell_counter += 1
            current_electrons = 0
        electrons_counter -= 1
    else:
        filled_shells.append(electrons_counter)
        if current_electrons > 0:
            filled_shells.append(current_electrons)
        break
print(filled_shells)
