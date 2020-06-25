# Умножение двоичных чисел
# Поддубняк Д. 6.1219-2
# Функции: __init__ = конструктор класса,обьявляет переменные, binarconverter = конвертор в двоичный вид,
# multiply = метод умножения двоичных чисел, minichecker = метод формулы чисел для рассчетов,
# bigger = метод определения большего числа(по длинне)


class Digits:
    def __init__(self, first_digit, second_digit):
        """Конструктор класса,объявляет переменные"""
        self.first_digit = str(first_digit)
        self.second_digit = str(second_digit)
        self.straight_first = self.binarconverter(self.first_digit) # Перевод в двоичную
        self.straight_second = self.binarconverter(self.second_digit) # Перевод в двоичную
        self.bigger_digit = self.bigger(self.straight_first, self.straight_second) # Узнаем какое число больше
        self.multiply_result = self.multiply(self.straight_first, self.straight_second) # Вызов метода умножения

    def __repr__(self): # Коррекция вывода на экран:
        return f"""Первое число в двоичном виде: {self.straight_first}\n
Второе число в двоичном виде: {self.straight_second}\n
Результат умножения: {self.multiply_result}"""

    def binarconverter(self, x, res=''):  # перевод десятичного числа в двоичную СС.
        x = str(x)
        if '-' in x: # Если отрицательное
            x1 = '-'
            x = int(x.replace('-', ''))
            if x == 0:
                return '0'
            else:
                while x > 0:
                    res = ('0' if x % 2 == 0 else '1') + res  # Формула перевода в бинарный вид
                    x //= 2
                return str(res)
        else: # Если положительное
            x = int(x)
            if x == 0:
                return '0'
            else:
                while x > 0:
                    res = ('0' if x % 2 == 0 else '1') + res  # Формула перевода в бинарный вид
                    x //= 2
                return str(res)

    def multiply(self, a, b):
        all_digits = [] # Словарь для записи вычислений
        b1 = list(map(int, b)) # Словарь из цифр второго числа
        counter = 0 # Счётчик
        for i in range(-1, ~(self.bigger_digit + self.minichecker(self.bigger_digit)), -1): # Цикл в обратном порядке
            if b1[i] == 0: # Если 0
                all_digits.append(0) # В словарь записываем 0
                counter += 1 # Счётчик растет
            elif b1[i] == 1: # Если 1
                a2 = int(a) * (10 ** counter) # Умножаем множимое на 10 в степени сноса влево
                all_digits.append(a2) # Заносим итог в словарь
                counter += 1 # Счётчик растет
        for i in range(len(all_digits) - 1): # Удаляем из словаря все лишние 0
            if all_digits[i] == 0:
                del all_digits[i]
        all_digits1 = list(map(str, all_digits)) # Делаем еще один словарь из предыдущего
        answer = 0
        for i in all_digits1:
            answer += int(i, 2) # Складываем элементы словаря
        answer = self.binarconverter(answer) # Возвращаем итог
        return answer

    def minichecker(self, a): # Счётчик последовательности,для определения длинны и формулы множимого и множителя
        b = 3

        for i in range(1, 9):
            b -= 1
            if i == a:
                return b

    def bigger(self, a, b): # Какое число больше
        return len(a) if len(a) > len(b) else len(b)


first = input("Введите множимое:\n")
second = input("Введите множитель:\n")
a = Digits(first, second) # Объявляю объект класса
print(a) # Вывод класса на экран(выведет метод для коррекции вывода класса)
