money_list = input().split(', ')
number_of_beggars = int(input())
final_sums = []
starting_index = 0
money_list_as_digyt = []
for element in money_list:
    money_list_as_digyt.append(int(element))
while starting_index < number_of_beggars:
    sum_for_current_beggar = 0
    for current_index in range(starting_index, len(money_list_as_digyt), number_of_beggars):
        sum_for_current_beggar += money_list_as_digyt[current_index]
    final_sums.append(sum_for_current_beggar)
    starting_index += 1
print(final_sums)


