import math

# Задача 1
# Напишите код, который принимает значения основания и высоты прямоугольного треугольника и
# печатает его площадь. Каждое число принимается на отдельной строке

# katet = int(input("Введите основание: "))
# katet2 = int(input("Введите высоту: "))

# print(katet * katet2 / 2)

# Задача 2
# Школа решила заменить столы в трех классах. За каждым столом сидят два ученика. 
# Учитывая количество учеников в каждом классе, напечатайте минимально возможное количество столов, которые нужно приобрести. 
# Программа должна принять три целых числа: количество учащихся в каждом из трех классов, a, b и c соответственно.
# Например, в первом классе 20 учеников и, следовательно, класс нуждается в 10 столах. Второй класс
# состоит из 21 ученика, поэтому им нужно не менее, чем 11 столов. 11 столов также достаточно для
# третьего класса из 22 учеников. Так что нам нужно всего 32 стола.

# a = int(input("Введите кол-во учеников из 1 класса: "))
# b = int(input("Введите кол-во учеников из 2 класса: "))
# c = int(input("Введите кол-во учеников из 3 класса: "))

# table_for_a = a / 2
# table_for_b = b / 2
# table_for_c = c / 2

# print(f"Количество столов {math.ceil(table_for_a)}, {math.ceil(table_for_b)}, {math.ceil(table_for_c)}")

# Задача 3
# Вам даны три переменные с фамилиями разных людей. Составьте и выведите на экран слово из символов в таком порядке:
# Третий символ из первой строки
# Второй символ из второй строки
# Четвертый символ из третьей строки
# Пятый символ из второй строки
# Третий символ из второй строки
# Попробуйте использовать интерполяцию: внутри фигурных скобок можно помещать не только целые переменные, но и отдельные символы с помощью квадратных скобок.

# first_surname = str(input("Введите первую фамилию: "))
# second_surname = str(input("Введите вторую фамилию: "))
# third_surname = str(input("Введите третью фамилию: "))

# print(f"Третий символ из первой строки: {first_surname[2]}")
# print(f"Второй символ из второй строки: {second_surname[1]}")
# print(f"Четвертый символ из третьей строки: {third_surname[3]}")
# print(f"Пятый символ из второй строки: {second_surname[4]}")
# print(f"Третий символ из второй строки: {second_surname[2]}")