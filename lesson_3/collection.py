# Задача 1
# На вход подаётся строка из целых уникальных чисел разделённых пробелами.
# Напечатайте числа, поменяв минимальное и максимальное число местами.
import collections


def swap_min_max(numbers):
    min_index = 0
    max_index = 0
    for i, number in enumerate(numbers):
        if number < numbers[min_index]:
            min_index = i
        elif number > numbers[max_index]:
            max_index = i

    numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
    return numbers


numbers = [5, 2, 9, 4, 7]
swapped_numbers = swap_min_max(numbers)
print(swapped_numbers)


# Задача 2
# На вход подаётся целое число N - количество записей в словаре.
# Далее подаются N пар: фамилия кандидата в президенты и число проголосовавших.
# Задача посчитать и вывести фамилии кандидатов с общим числом, которое они набрали.
# Фамилии вывести в алфавитном порядке.


def print_candidates(n):
    votes_dict = {}
    for i in range(n):
        name = input("Введите фамилию кандидата: ")
        votes = int(input("Введите число проголосовавших: "))
        votes_dict[name] = votes
        print(votes_dict)
    sorted_candidates = sorted(votes_dict.items(), key=lambda x: x[1], reverse=True)
    for candidate in sorted_candidates:
        print(f"{candidate[0]}: {candidate[1]}")

n = 3

print_candidates(n)

#
# Задача 3
# Список на 10 элементов, заполненный случайными числами от 1 до 20.
# Необходимо на основе данного списка создать новый список,
# в котором четные элементы первого списка умножены на 2, а нечетные на 3.
# Использовать функции map() и лямбда.
# Вывести первоначальный список и получившийся список.
# Пример:
# первый список: [1, 2, 3, 4]
# получившийся список: [3, 4, 9, 8]

import random

numbers = [random.randint(1, 20) for _ in range(10)]

even_multiplier = lambda x: x * 2 if x % 2 == 0 else x * 3
modified_numbers = list(map(even_multiplier, numbers))

print("Первый список:", numbers)
print("Получившийся список:", modified_numbers)
