"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
import numpy as np

# Функция для оценки. 
# Эта функция необходима, чтобы определить, 
# за какое число попыток программа угадывает наше число.
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    return score

# Подход 1: Случайное угадывание
def random_predict(number: int = 1) -> int:
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали

    return count

# Подход 2: Угадывание с коррекцией
def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)

    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count

# Подход 3: Метод бинарного поиска с оценкой сложности log2N
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    num_min = 1
    num_max = 100
    
    # Нужно установить значение "1", 
    # т.к. если будет сразу выход из цикла, 
    # то к тому времени уже пройдёт одно вычисление и одно сравнение
    count = 1
    
    # Начинаем с проверки числа в середине диапазона
    num_cur = (num_min + num_max) // 2
    
    while (num_cur != number):
        # Увеличиваем счётчик на 1,
        # т.к. впереди ещё одно повторение вычисления и проверки
        count += 1
        
        # Переводим проверку в нижнюю половину диапазона
        if (num_cur > number):
            num_max = num_cur - 1
        # Переводим проверку в верхнюю половину диапазона
        else:
            num_min = num_cur + 1

        # Берём число в середине диапазона
        num_cur = (num_min + num_max) // 2

    # Ваш код заканчивается здесь

    return count

if __name__ == "__main__":
    # RUN
    print ("Вариант №1. ", end='')
    score_game(random_predict)
    print ("Вариант №2. ", end='')
    score_game(game_core_v2)
    print ("Вариант №3. ", end='')
    score_game(game_core_v3)
