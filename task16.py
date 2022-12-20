# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, 
# которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 1

# 1 2 1 2 2
# Вывод: 2

n = int(input('Введите длину списка: '))
if n <= 0:
    print('Недопустимый формат числа.')
else:
    print('Получившийся массив: ')
    import random      
    randomList = []
    for elements in range(1, n + 1):
        randomList.append(random.randint(0, n // 2))
    print(randomList)
    print('')

    x = int(input('Введите число, которое необходимо проверить: '))

    count = 0
    for el in randomList:
        if el == x:
            count += 1
    print(f'В построенном списке количество элементов со значением {x}: {count}.')
