my_list = [1, 3, 5, 8]
print(my_list.index(3))
command_index = my_list.index(3)
pin_command = my_list.pop(command_index)
print(my_list)
my_list.append(pin_command)
print(my_list)
