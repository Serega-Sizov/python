# ЗАДАЧА №1
# number = input('Введите число: ')
# resualt = int(number) + 2
# print(resualt)


# number = int(input('Введите число: '))
# resualt = number + 2
# print(resualt)


# Задача №2 
# num = int(input('Введите число: '))
# if num < 0:
#     print('Ввели не верное число, введите от 0 до 10')
# elif num > 10:
#     print('Ввели не верное число, введите от 0 до 10')
# else:
#     print('Число введено ВЕРНО в диапазоне от 0 до 10')
#     print('Введенное число в квадрате равно:', num**2)

# Задача №2 через цикл while
# while True:
#     num = int(input('Введите число: '))
#     if num > 0 and num <= 10:
#         print('введенное число в квадрате равно ', num**2)
#         break
#     else:
#         print('введите число от 0 до 10')


# Задача №3
# print('!!!!!!!!!!!!!!!МЕДИЦИНСКАЯ КАРТОЧКА!!!!!!!!!!!')
# name = input('Введите имя: ')
# suname = input('Введите фамилию: ')
# age = int(input('Введите ваш возраст: '))
# weight = int(input('Введите ваш вес: '))

# # "...если ему до 30 лет и вес от 50 и до 120 кг..."
# if age <= 30 and 50 <= weight <= 120:
#     print(name, suname, age, 'год', 'вес', weight, '-пациент в хорошей форме')
# # "...если ему более 30 и вес меньше 50 или больше 120 кг..."
# elif (30 < age < 40) and (weight < 50 or weight > 120):
#     print(name, suname, age, 'год', 'вес', weight, '-пациенту необходимо заняться собой')
# # "...если ему более 40 и вес менее 50 или больше 120..."
# elif (age >= 40) and (weight < 50 or weight > 120):
#     print(name, suname, age, 'год', 'вес', weight, '-пациенту требуется врачебный осмотр')
# else:
#     print('Пациент в удовлетворительном состоянии')
# input()

# Задача№5 (Игра угадай число)
# number = 28
# num = int(input('Введите число: '))
# if num == number:
#     print('Вы угадали число')
# else:
#     if num > number:
#         print('Вы ввели число больше задуманного')
#     elif 26 <= num <= 29:
#         print('Вы рядом')
#     elif num < number:
#         print('Вы ввели число меньше задуманного')
# input()


# Задача№5 (Игра угадай число) через цикл while
# number = 27
# num = int(input('Введите число от 1 до 100: '))

# while num != number:
#     print('Вы не угадали число, попробуйте еще раз')
#     num = int(input('Введите число от 1 до 100: '))
# print('Поздравляю, Вы угадали число')


# Задача №6 (вывести числа от 0 до 100)
# num = 0
# while num <= 100:
#     print(num)
#     num = num + 1
# input()

# Задача №7 (вывести числа от 0 до n)
# num = 0
# number = int(input('Введите число: '))
# while num <= number:
#     print(num)
#     num = num + 1


# Задача №8 (вывести только четные числа от 0 до n)
# num = 0
# n = int(input('Введите n: '))
# while num <= n:
#     if num % 2 == 0:
#         print(num)
#     num = num + 1
