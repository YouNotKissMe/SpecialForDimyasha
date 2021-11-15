import os


def RLE():
    numberOfRepetitions = 1
    massiveLetters = []
    massiveRepetitionsLetters = []
    peremennaya = None

    for i in range(len(text)):

        if peremennaya:
            if text[i] == peremennaya:
                if i + 1 == len(text):
                    massiveLetters.append(peremennaya)
                    numberOfRepetitions += 1
                    massiveRepetitionsLetters.append(numberOfRepetitions)
                numberOfRepetitions += 1

            else:
                if i + 1 == len(text):
                    massiveLetters.append(peremennaya)
                    massiveRepetitionsLetters.append(numberOfRepetitions)

                    massiveLetters.append(text[i])
                    massiveRepetitionsLetters.append(1)
                else:
                    massiveLetters.append(peremennaya)
                    massiveRepetitionsLetters.append \
                        (numberOfRepetitions)
                    peremennaya = text[i]
                    numberOfRepetitions = 1

        else:
            peremennaya = text[i]
    # print(massiveLetters, massiveRepetitionsLetters)
    text1 = ""
    RLEtext = open('file/rle.txt', 'w')
    for i in range(len(massiveLetters)):
        text1 += f"{massiveRepetitionsLetters[i]}" \
                 f"{massiveLetters[i]}"

    RLEtext.write(text1)
    RLEtext.close()
    return massiveLetters, massiveRepetitionsLetters


def AntiRLE():
    a, b = RLE()
    antiRLEtext = open('file/antirle.txt', 'w')
    qnm = ''
    for i in range(len(a)):
        qnm += a[i] * b[i]
    antiRLEtext.write(qnm)
    antiRLEtext.close()


text = open('file/usual.txt', 'r',encoding='utf-16').read()
size1 = os.stat('file/usual.txt').st_size
print(f'исходный размер файла {size1} байт\n')
try:
    a = int(input('каким алгоритмом сжатия вы хотите воспользоватся?\n'
                  'набирите 1, если хотите сжать алгоритмом RLE\n'
                  'набиирте 2,если хотите сжать Алгоритмом Лемпеля'
                  ' Зива\n Ваше число: '))
    if a == 1:
        AntiRLE()
        size2 = os.stat('file/rle.txt').st_size
        print(f'получившийся после RLE размер файла {size2}')
        qqq = size1 / size2
        print(f'кф сжатия {qqq}')


    elif a == 2:
        print('В разработке')
    else:
        print('Вы ввели не то число')
except ValueError:
    print('Error: Вы ввели не число')