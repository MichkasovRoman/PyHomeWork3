# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве 
# и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, 
# которые равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

n = int(input('Введите длину списка: '))
print('Получившийся список: ')
import random      
randomList = []
for elements in range(0, n):
    randomList.append(random.randint(1, n))
print(randomList)

print('')

x = int(input('Введите число, которое необходимо проверить: '))

if x in randomList:
    print(f'Ближайшим к {x} числом в списке является само это число.')
else:
    randomList.append(x)
    setArr = set(randomList)   # таким нехитрым способом я удаляю из списка повторяющиеся элементы   
    listSet = list(setArr)     # и упорядочиваю элементы нового списка по возрастанию   
    lastInd = len(listSet) - 1

    if listSet[0] == x:
        print(f'Элемент списка, ближайший к числу {x}:\n{listSet[1]}')
    elif listSet[lastInd] == x:
        print(f'Элемент списка, ближайший к числу {x}:\n{listSet[lastInd - 1]}')
    else:
        i = 1
        temp1 = 0
        temp2 = 0
        while i <= lastInd - 1:
            if listSet[i] == x:
                temp1 = listSet[i - 1]
                temp2 = listSet[i + 1]
            i = i + 1
            
        if x - temp1 <= temp2 - x:
            print(f'Элемент списка, ближайший к числу {x}:\n{temp1}')
        else:
            print(f'Элемент списка, ближайший к числу {x}:\n{temp2}') 

    
