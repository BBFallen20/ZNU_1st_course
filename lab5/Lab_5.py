# Лабораторная работа №5
# Поддубняк Д.
# Функции: literator = перевод цифр в символы,Solution = перевод чисел в СС.(по частям)
# Переменные: from_system = исходная СС,system = итоговая СС,x = погрешность,number = число




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


print("=" * 50)
print("\t\tЛабораторная работа №5")
print("\t\tПоддубняк Д.")
print("=" * 50)
while True:
    print('''Выберите действие:
1.Начать работу
2.Выход''')
    what = input()
    if what == "1":
        try:
            from_system = int(input("Введите систему счисления вашего числа(2-16):"))
            if from_system >= 2 and from_system <= 16:
                pass
            else:
                print("Неверно введена система счисления.")
                continue
        except ValueError:
            print("Неверно введена система счисления.")
            continue
        try:
            system = int(input("Введите систему счисления для перевода(2-16):"))
            if system >= 2 and system <= 16:
                pass
            else:
                print("Неверно введена система счисления.")
                continue
        except ValueError:
            print("Неверно введена система счисления.")
            continue
        try:
            x = int(input("Введите количество символов после запятой:"))
            if x <= 0:
                print("Ошибка ввода чисел после запятой.")
                continue
            else:
                pass
        except ValueError:
            print("Ошибка ввода чисел после запятой.")
            continue
        number = input("Введите число для перевода:")
        number = str(number)
        try:
            print(Solution(from_system, system, x, number))
        except ValueError:
            print("Ошибка совпадения числа с его СС|символов после запятой.")
            continue
    elif what == "2":
        exit()
    else:
        print("Неверно выбрано действие.")
