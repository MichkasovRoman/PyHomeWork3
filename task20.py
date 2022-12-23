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
        1: 'АВЕИНОРСТAEIOULNSTR', 
        2: 'ДКЛМПУDG', 
        3: 'БГЁЬЯBCMP', 
        4: 'ЙЫFHVWY', 
        5: 'ЖЗХЦЧK', 
        8: 'ШЭЮJX', 
        10: 'ФЩЪQZ'
    }

def WordOrNot(string):             # метод проверяет, является ли введенная пользователем строка словом
    stringList = list(string)
    for elements in stringList:
        if 65 < ord(elements.upper()) < 90 or 192 < ord(elements.upper()) < 223:
            return True
    return False

def CyrillicOrLatin(string):       # метод проверяет, состоит ли слово из букв одного алфавита
    stringList = list(string)
    newlist = sorted(list(word.upper()))
    if 65 < ord(newlist[0]) < 90 and 192 < ord(newlist[len(newlist) - 1]) < 223:
        return False
    return True

word = input('Введите слово, написанное латиницей или кириллицей: ')
if WordOrNot(word):
    print('Вы ввели не слово.')
elif CyrillicOrLatin(word):
    print('Ваше слово состоит из букв, взятых из различных алфавитов.')
else:
    print('отлично')

# k = int(input())
# if k in lettersDictionary.keys:
#     spisok = list(lettersDictionary[k])
# print(spisok)
    

# lettersToNumbers = []
# for letters in wordList:
#     for k in lettersDictionary.keys():
#          if letters.upper() in k:
#               lettersToNumbers.append(lettersDictionary[k])

# print(sum(lettersToNumbers))