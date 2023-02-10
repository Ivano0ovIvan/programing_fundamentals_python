my_list = []
for _ in range(3):
    command = input()
    my_list.append(command)
my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)
