count_of_numbers = int(input())
even_list = []
odd_list = []
negative_list = []
positive_list = []
for i in range(count_of_numbers):
    current_number = int(input())
    if current_number % 2 == 0:
        even_list.append(current_number)
    if current_number % 2 != 0:
        odd_list.append(current_number)
    if current_number < 0:
        negative_list.append(current_number)
    if current_number >= 0:
        positive_list.append(current_number)
command = input()
my_list = []
if command == 'even':
    my_list = even_list
elif command == 'odd':
    my_list = odd_list
elif command == 'negative':
    my_list = negative_list
elif command == 'positive':
    my_list = positive_list
print(my_list)