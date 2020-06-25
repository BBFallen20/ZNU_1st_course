import time
"""Описание:
Калькулятор выполняет обычные арифметические операция над двумя вводимыми числами в произвольных СС
Ответ можно получить в произвольной СС
Операции производятся над отрицательными и дробными числами в том числе.
Выполнил:
Поддубняк Д.
Группа 6.1219-2
Приятного пользования!"""

def literator(Num): # Перевод цифр в буквенные соответствия СС.
    Num = list(Num.upper()) # Число переводится в список(упрощенный вывод)
    while "A" in Num:
        NumIndex = Num.index('A')
        Num[NumIndex] = '10'

    while "B" in Num:
        NumIndex = Num.index('B')
        Num[NumIndex] = '11'

    while "C" in Num:
        NumIndex = Num.index('C')
        Num[NumIndex] = '12'

    while "D" in Num:
        NumIndex = Num.index('D')
        Num[NumIndex] = '13'

    while "E" in Num:
        NumIndex = Num.index('E')
        Num[NumIndex] = '14'

    while "F" in Num:
        NumIndex = Num.index('F')
        Num[NumIndex] = '15'
    return (Num)


def Solution(SystemNum, OutputNum, Accuracy, Num):
    Num = str(Num)
    NumRow = '0123456789ABCDEF' # Алфавит(ограничение перевода до 16 СС.)
    try:
        dot = Num.index('.') - 1  # Получение индекса точки для вычислений
        k = literator(Num) # Коррекция цифр в буквенные индексы
        item = '.'
        if item in k:
            k.remove(item)
        k = list(map(str, k))
        k = list(map(int, k))
        # Исключение постороних символов (!"№;%:?*()" и.т.д)
    except ValueError:
        return "Неверно введено число."
    else:

        # Перевод в 10-ю систему СС для дальнешего перевода
        Res = 0

        for elem in k:
            Res += int(elem) * (SystemNum ** dot)
            dot -= 1
        Res = str(Res)

        # Отделение целой части от дробной
        firstdigit, seconddigit = Res.split('.')
        firstdigit = int(firstdigit) # Целая часть
        seconddigit = int(seconddigit) / 10 ** (len(seconddigit)) # Дробная часть

        # Используется для упрощенного совмещения частей числа
        IntPartList = [] # Список целой части числа
        FracPartList = [] # Список дробной части числа
        # Перевод целой части
        while firstdigit != 0:
            IntPartList.append(NumRow[firstdigit % OutputNum]) # Ввод в список целой части
            firstdigit = firstdigit // OutputNum
        # #Перевод дробной части
        for j in range(Accuracy):
            for i in str(seconddigit):
                seconddigit = seconddigit * OutputNum
                if seconddigit < 1:
                    FracPartList.append(NumRow[int(seconddigit)]) # Ввод в список дробной части
                else:
                    FracPartList.append(NumRow[int(seconddigit)])
                    sdstr = str(seconddigit)
                    sdstr = sdstr.split('.')
                    seconddigit = int(sdstr[1]) / 10 ** (len(sdstr[1]))
    return ("".join(map(str, IntPartList[::-1])) + '.' + "".join(map(str, FracPartList[:Accuracy:1]))) # Возврат итога производится в строке



def continued(num):
    while True:
        print('=' * 50)
        mode = input('''Выберите действие:
1.Продолжить вычисления.
2.Новое число.
3.Выход.\n''')
        print('=' * 50)
        if mode == '1':
            todo = input("Введите действие(+, -, *, /):\n")
            second_system = int(input("Введите систему счисления второго числа:\n"))
            if second_system <= 16 and second_system >= 2: # Ограничение СС
                second_digit = input("Введите второе число:\n")
                if '.' in second_digit: # Если число дробное
                    if '-' in second_digit: # Если отрицательное
                        split = second_digit.split('-', 2) # Отделение минуса от числа
                        split[0] = '-'
                        second_digit = split[1] # Число отделено от минуса
                        second_d = float(split[0] + Solution(second_system, 10, 2, second_digit)) # Перевод числа
                    else:
                        second_d = float(Solution(second_system, 10, 2, second_digit)) # Перевод числа
                else:
                    # Перевод целочисленно если число не дробное
                    second_d = int(convertor(second_digit, 10, second_system))
                try:
                    # Выбор действия между числами
                    if todo == "+":
                        # Сложение
                        res = addition(num, second_d)
                    elif todo == "-":
                        # Вычитание
                        res = subtraction(num, second_d)
                    elif todo == "*":
                        # Умножение
                        res = multiplication(num, second_d)
                    elif todo == "/":
                        # Деление
                        res = division(num, second_d)
                    else:
                        print("Неверно выбрано действие.")
                        break
                    try:
                        ss = int(input("Введите систему счисления для ответа:\n"))
                        if ss <= 16 and ss >= 2:
                            new_res = str(res)
                            if '.' in new_res: # Если дробное
                                if '-' in new_res: # Если отрицательное
                                    split = new_res.split('-',2) # Отделение минуса
                                    split[0] = '-'
                                    new_res = split[1] # Число без минуса
                                    result = split[0] + Solution(10, ss, 2, new_res) # Соединение минуса с переводом
                                else:
                                    result = Solution(10, ss, 2, new_res) # Перевод числа
                            else:
                                result = convertor(new_res, ss) # Целочисленный перевод если не дробное
                            print('=' * 50)
                            print(f"Ответ: {result}")
                            print('=' * 50)
                            time.sleep(2) # Задержка вывода
                            continued(res) # Рекурсия функции-продолжения
                        else:
                            print("Неверно введена СС.Макс-16,Мин-2.")
                            break
                    except Exception:
                        print("СС от 2 до 16")
                        break
                except Exception:
                    print("Ошибка")
                    break
            else:
                print("Неверно введена СС.Макс-16,Мин-2.")
                break
        elif mode == '2':
            break # Окончание работы
        else:
            exit() # Окончание работы

def start():
    first_system = int(input("Введите систему счисления вашего числа:\n"))
    if first_system <= 16 and first_system >= 2: # Ограничение СС
        first_digit = input('Введите первое число:\n')
        if '.' in first_digit: # Если дробное
            if '-' in first_digit: # Если отрицательное
                split = first_digit.split('-', 2) # Отделение минуса от числа
                split[0] = '-'
                first_digit = split[1] # Число без минуса
                first_d = float(split[0] + Solution(first_system, 10, 2, first_digit)) # Перевод числа
            else:
                first_d = float(Solution(first_system, 10, 2, first_digit)) # Перевод числа
        else:
            first_d = int(convertor(first_digit, 10, first_system)) # Целочисленный перевод если не дробное
        todo = input("Введите действие(+, -, *, /):\n") # Выбор действия
        second_system = int(input("Введите систему счисления второго числа:\n"))
        if second_system <= 16 and second_system >= 2: # Ограничение СС
            second_digit = input("Введите второе число:\n")
            if '.' in second_digit: # Если дробное
                if '-' in second_digit: # Если отрицательное
                    split = second_digit.split('-', 2) # Отделение минуса от числа
                    split[0] = '-'
                    second_digit = split[1] # Число без минуса
                    second_d = float(split[0] + Solution(second_system, 10, 2, second_digit)) # Перевод числа
                else:
                    second_d = float(Solution(second_system, 10, 2, second_digit)) # Перевод числа
            else:
                second_d = int(convertor(second_digit, 10, second_system)) # Целочисленный перевод если не дробное
            try:
                if todo == "+":
                    res = addition(first_d, second_d)
                elif todo == "-":
                    res = subtraction(first_d, second_d)
                elif todo == "*":
                    res = multiplication(first_d, second_d)
                elif todo == "/":
                    res = division(first_d, second_d)
                else:
                    print("Неверно выбрано действие.")
                try:
                    ss = int(input("Введите систему счисления для ответа:\n"))
                    if ss <= 16 and ss >= 2:
                        new_res = str(res)
                        if '.' in new_res:  # Если дробное
                            if '-' in new_res:  # Если отрицательное
                                split = new_res.split('-', 2)  # Отделение минуса
                                split[0] = '-'
                                new_res = split[1]  # Число без минуса
                                result = split[0] + Solution(10, ss, 2, new_res)  # Соединение минуса с переводом
                            else:
                                result = Solution(10, ss, 2, new_res)  # Перевод числа
                        else:
                            result = convertor(new_res, ss)  # Целочисленный перевод если не дробное
                        print('='*50)
                        print(f"Ответ: {result}")
                        print('=' * 50)
                        time.sleep(2)
                        continued(res)
                    else:
                        print("Неверно введена СС.Макс-16,Мин-2.")
                except Exception:
                    print("Неверно введена СС.Макс-16,Мин-2.")
            except Exception:
                print("Ошибка.")
        else:
            print("Неверно введена СС.Макс-16,Мин-2.")
    else:
        print("Неверно введена СС.Макс-16,Мин-2.")



def convertor(num, to_base=10, from_base=10):
    """Функия целочисленного перевода"""
    try:
        num = str(num)
        if '-' in num: # Если отрицательное
            split = num.split('-',2) # Отделение минуса
            split[0] = '-'
            num = split[1] # Действия с числом без минуса
            if isinstance(num, str):
                n = int(num, from_base)
            else:
                n = int(num)
            alphabet = "0123456789ABCDEF"
            if n < to_base:
                return split[0] + alphabet[n] # Возврат итога с минусом
            else:
                return split[0] + convertor(n // to_base, to_base) + alphabet[n % to_base] # Возврат итога с минусом
        else:
            if isinstance(num, str):
                n = int(num, from_base)
            else:
                n = int(num)
            alphabet = "0123456789ABCDEF"
            if n < to_base:
                return alphabet[n]
            else:
                return convertor(n // to_base, to_base) + alphabet[n % to_base]
    except(ValueError):
        return "Ошибка совпадения числа с его СС."


def addition(a, b):
    c = a + b
    return c


def subtraction(a, b):
    c = a - b
    return c


def multiplication(a, b):
    c = a * b
    return c


def division(a, b):
    c = a / b
    return c


view = "=" * 50
print('''{0}
Calculator by Poddubnjak D.
Float digits may be rounded!
{1}'''.format(view, view))

while True:
    print('=' * 50)
    print("Выберите действие:")
    print("1.Начать работу.")
    print("Exit-выход.")
    print('=' * 50)
    starter = input('\n')
    if starter == "Exit":
        exit()
    elif starter == '1':
        start()
