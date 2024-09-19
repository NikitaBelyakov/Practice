import random

# # Задание 1
# num_list = [5, 19, 23, 9, 100]
# print(num_list)
# reverse_num_list = num_list[::-1]
# print(reverse_num_list)

# # Задание 2
# first_list = [random.randint(0, 50) for _ in range(5)]
# second_list = [random.randint(0, 50) for _ in range(5)]
# print(first_list, '\n', second_list)
# third_list = first_list[::2] + second_list[1::2]
# print(third_list)

# # Задание 3
# data_list = [5, 3.14, 5.6, 19, '100', '5.6',  23, '11', 18.3, 9, 100, '5']
# print(data_list)
# new_data_list = set(data_list)
# print(new_data_list)

# # Задание 4
# d = {
#     'Первый': 5,
#     'Второй': 19,
#     'Третий': 54,
#     'Четвертый': 5,
#     'Пятый': 54,
#     'Шестой': 27,
#     'Седьмой': 19,
#     'Восьмой': 27
# }
# print('Ваш словарь:\n', d)
# first_tuple = (5, ['Первый', 'Четвертый'])
# second_tuple = (19, ['Второй', 'Седьмой'])
# third_tuple = (54, ['Третий', 'Пятый'])
# fourth_tuple = (27, ['Шестой', 'Восьмой'])
# new_list = [(first_tuple)] + [(second_tuple)] + [(third_tuple)] + [(fourth_tuple)]
# print('Ваш список кортежей:\n', new_list)

# Задание 5
dict_1 = {
    'Первый': 5,
    'Второй': 19,
    'Третий': 54,
    'Четвертый': 5,
    'Пятый': 54,
    'Шестой': 27,
    'Седьмой': 19,
    'Восьмой': 27
}
dict_2 = {
    '1': 13,
    '2': 19,
    '3': 5,
    '4': 20,
    '5': 97,
    '6': 19,
    '7': 78,
    '8': 7
}
print('Ваши словари:\n', dict_1, '\n', dict_2)

same = set(dict_1.values()).intersection(set(dict_2.values()))
new_dict = {}
for i_key, i_val in dict_1.items():
    if i_val in same:
        new_dict[i_key] = i_val
for i_key, i_val in dict_2.items():
    if i_val in same:
        new_dict[i_key] = i_val
print('Ваш новый словарь:\n', new_dict)