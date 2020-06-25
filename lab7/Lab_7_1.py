# Лабораторная работа №6
# Поддубняк Д.
# Функции: binarconverter = перевод из 10 СС в 2 СС, straight_code = перевод в прямой код, additinally_code = перевод в дополнительный код
# reverse_code = перевод в обратный код, plus = сложение, minus = вычитание
# Переменные:decimal_digit = исходное число в 10 СС, straight_view = число в прямом коде, additinally_view = число в дополнительном коде
# reverse_view = число в обратном коде, ispos_a, ispos_b = числа в десятичном виде для сравнений
import time


def big_digit(num, ispositive='+'):
    l = len(num)  # Длинна числа
    if ispositive == '-':  # Если отрицательное:
        num = '1' + ('0' * (16 - l - 1)) + num
    else:  # Если положительное:
        num = '0' + ('0' * (16 - l - 1)) + num
    return num


def checker(decimal_digit):
    if decimal_digit > 127 or decimal_digit < -127:
        decimal_digit = str(decimal_digit)
        if '-' in decimal_digit:  # Если число отрицательное:
            split = decimal_digit.split('-')  # Список для отделения минуса от числа
            split[0] = '-'  # Отделение минуса
            binar_digit = (binarconverter(split[1]))
            straight_view = big_digit(binar_digit, split[0])
            reverse_view = reverse_code(straight_view)
            print(f'''Число {decimal_digit} двоичном виде: {binar_digit}
В прямом коде: {straight_view}
В обратном коде: {reverse_view}
''')
            return reverse_view
        elif not '-' in decimal_digit:  # Если число положительное:
            binar_digit = binarconverter(decimal_digit)
            straight_view = big_digit(binar_digit)
            reverse_view = straight_view
            print(f'''Число {decimal_digit} двоичном виде: {binar_digit}
В прямом коде: {straight_view}
В обратном коде: {reverse_view}
''')
            return reverse_view
    else:
        main(str(decimal_digit))





def plus(a, b): # Принимает числа в обратном коде, числа в десятичной системе для сверок
    if a.startswith('1') and b.startswith('1'):
        a = int(a)
        b = int(b)
        p = (a + b)
        c = int(p / 2)
        answer = ''
        for i in str(c):
            i = int(i)
            i = i % 2
            answer += str(i)
        print(answer)
    else:
        a = int(a)
        b = int(b)
        p = (a + b) * 10
        c = int(p // 2)
        answer = ''
        for i in str(c):
            i = int(i)
            i = i % 2
            answer += str(i)
        print(answer)



def minus(a, b): # Принимает числа в обратном коде, числа в десятичной системе для сверок
    a = int(a)
    b = int(b)
    p = (a - b) * 10
    c = int(p / 2)
    answer = ''
    for i in str(c):
        i = int(i)
        i = i % 2
        answer += str(i)
    print(answer)

def main(decimal_digit):
    if '-' in decimal_digit:  # Если число отрицательное:
        split = decimal_digit.split('-')  # Список для отделения минуса от числа
        split[0] = '-'  # Отделение минуса
        binar_digit = (binarconverter(split[1]))
        straight_view = straight_code(binar_digit, split[0])
        reverse_view = reverse_code(straight_view)
        print(f'''Число {decimal_digit} двоичном виде: {binar_digit}
В прямом коде: {straight_view}
В обратном коде: {reverse_view}
''')
        return reverse_view
    elif not '-' in decimal_digit:  # Если число положительное:
        binar_digit = binarconverter(decimal_digit)
        straight_view = straight_code(binar_digit)
        reverse_view = straight_view
        print(f'''Число {decimal_digit} двоичном виде: {binar_digit}
В прямом коде: {straight_view}
В обратном коде: {reverse_view}
''')
        return reverse_view


def binarconverter(x, res=''):  # перевод десятичного числа в двоичную СС.
    x = int(x)
    if x == 0:
        return '0'
    else:
        while x > 0:
            res = ('0' if x % 2 == 0 else '1') + res  # Формула перевода в бинарный вид
            x //= 2
        return str(res)


def straight_code(num, ispositive='+'):
    l = len(num)  # Длинна числа
    if ispositive == '-':  # Если отрицательное:
        num = '1' + ('0' * (8 - l - 1)) + num
    else:  # Если положительное:
        num = '0' + ('0' * (8 - l - 1)) + num
    return num



def reverse_code(num):
    new_num = ''  # Переменная для коррекции
    num_part = ''
    if num[0] == '0':  # Инверсия путем добавления в переменную для коррекции итоговых значений
        num_part = num[0]
        num = num[1:]
    elif num[0] == '1':
        num_part = num[0]
        num = num[1:]
    for i in range(len(num)):
        if num[i] == '0':
            new_num += '1'
        elif num[i] == '1':
            new_num += '0'
    return num_part + new_num  # Соединение итогового числа с разрядной цифрой


print("=" * 50)
print('''Лабораторная работа №6
Поддубняк Д.''')
print("=" * 50)
while True:
    first_digit = input('Введите первое число в 10-ой СС(Не больше 127 и не меньше -127)\n')
    second_digit = input('Введите второе число в 10-ой СС(Не больше 127 и не меньше -127)\n')
    try:
        if int(first_digit) <= 127 and int(first_digit) >= -127:  # Ограничение числа(Конфигурабельно)
            try:
                converted_f_digit = main(first_digit)
                converted_s_digit = main(second_digit)
            except Exception:
                print("Неверно введено число.")
                continue
            todo = input('Введите операцию("-","+"):\n')
            if todo == '+':
                plus(converted_f_digit, converted_s_digit)
                time.sleep(2)
                continue
            elif todo == '-':
                minus(converted_f_digit, converted_s_digit)
                time.sleep(2)
                continue
            else:
                print("Неверно выбрана операция.")
                continue
        else:
            print("Система рассчитана на число меньше 128|болше -128")
            continue
    except Exception:
        print("Ошибка ввода.")
        continue