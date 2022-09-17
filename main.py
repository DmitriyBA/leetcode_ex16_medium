import random

alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
option = [1, 0]
str_word = input()
print(f"Допустимый диапазон индексов от {0} до {len(str_word) - 1}")
flag_1= True
while flag_1:
    index_start = int(input("Введите индекс начала сдвига: "))
    if (len(str_word) - 1) >= index_start >= 0:
        flag_1 = False
    else:
        flag_1 = True
        print(f"Допустимый диапазон индексов от {0} до {len(str_word) - 1}")

flag_2 = True
while flag_2:
    index_stop = int(input("Введите индекс конца сдвига: "))
    if (len(str_word) - 1) >= index_stop >= 0:
        flag_2 = False
    else:
        flag_2 = True
        print(f"Допустимый диапазон индексов от {0} до {len(str_word) - 1}")

direction = random.choice(option)
shifts = [index_start, index_stop, direction]


def shifts_letter_direction_right(str_word_: str, shifts_: list, alphabet_: list) -> str:
    """
     Функция принимает на вход:
     1. Слово
     2. Список сдвигов
     3. Алфавит
    """
    str_word_ = list(str_word_)
    for item in range(shifts_[0], shifts_[1]+1, 1):
        for letter in range(len(alphabet_)):
            if str_word_[item] == alphabet_[letter]:
                str_word_[item] = alphabet_[letter + 1]
                break
            else:
                continue
    return str_word_



def shifts_letter_direction_left(str_word__: str, shifts__: list, alphabet__: list) -> str:
    """
     Функция принимает на вход:
     1. Слово
     2. Список сдвигов
     3. Алфавит
    """
    str_word__ = list(str_word__)
    for item in range(shifts__[0], shifts__[1]+1, 1):
        for letter in range(len(alphabet__)):
            if str_word__[item] == alphabet__[letter]:
                str_word__[item] = alphabet__[letter - 1]
                break
            else:
                continue
    return str_word__


if direction == 1:
    print(shifts_letter_direction_right(str_word, shifts, alphabet))
elif direction == 0:
    print(shifts_letter_direction_left(str_word, shifts, alphabet))


