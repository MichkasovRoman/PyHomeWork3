# Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.

# Ввод: ноутбук
# Вывод: 12

lettersDictionary = \
    {
        'АВЕИНОРСТAEIOULNSTR': 1, 
        'ДКЛМПУDG': 2, 
        'БГЁЬЯBCMP': 3, 
        'ЙЫFHVWY': 4, 
        'ЖЗХЦЧK': 5, 
        'ШЭЮJX': 6, 
        'ФЩЪQZ': 7
    }

def WordOrNot(string):             # метод проверяет, является ли введенная пользователем строка словом
    stringList = list(string)
    for element in stringList:
        if not 65 <= ord(element.upper()) <= 90 and not 1040 <= ord(element.upper()) <= 1071:
            return False
    return True
    

def CyrillicOrLatin(string):       # метод проверяет, состоит ли слово из букв одного алфавита
    stringList = list(string)
    newlist = sorted(list(word.upper()))
    if 65 <= ord(newlist[0]) <= 90 and 1040 <= ord(newlist[len(newlist) - 1]) <= 1071:
        return False
    return True

word = input('Введите слово, написанное латиницей или кириллицей: ')

if not WordOrNot(word):
    print('Вы ввели не слово.')
elif not CyrillicOrLatin(word):
    print('Ваше слово состоит из букв, взятых из различных алфавитов.')
else:
    lettersToNumbers = []
    for letter in list(word):
        for key in lettersDictionary.keys():
            if letter.upper() in key:
                lettersToNumbers.append(lettersDictionary[key])
    print(f'Стоимость введенного вами слова: {sum(lettersToNumbers)}')
