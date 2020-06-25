"""Лабораторная работа №10 Поддубняк Д. 6.1219-2
Классы: Digits - основной класс
Функции: __init__ = конструктор класса, __repr__ = редактор вывода на экран, binarconverter = функция деления.
Переменные: digit = делимое, divider = делитель, answer = результат деления."""


class Digits:
    """Объявляю класс чисел"""
    def __init__(self, digit, divider):
        """Конструктор класса,объявляет переменные,хранит в общем доступе"""
        self.digit = str(digit) # Делимое
        self.divider = str(divider) # Делитель
        self.converted = int(self.binarconverter(self.digit)) # Делимое в двоичном виде
        self.div = int(self.binarconverter(self.divider)) # Делитель в двоичном виде
        self.answer = self.binarconverter(self.converted, self.div) # Ответ в двоичном виде

    def __repr__(self):
        """Функция вывода при запросе вывода данных класса на экран"""
        return f"<Digit {self.converted}|Divider {self.div}|Answer {self.answer}>"

    def binarconverter(self, x, y=2):  # перевод десятичного числа в двоичную СС.
        """Суть: с помощью функции из 2ой лабораторной работы(перевод в двоичную систему) производится
        целочесленное деление первого числа на второе, при остатке записывается 1, иначе - 0
        x = делимое, y = делитель"""
        try:
            x = int(x)
            res = ''
            if x == 0:
                return '0'
            else:
                while x > 0:
                    res = ('0' if x % y == 0 else '1') + res  # Формула перевода в бинарный вид
                    x //= y
                return str(res)
        except ZeroDivisionError:
            # На ноль не делить!
            return "На ноль делить нельзя."


a = Digits(12, 0)
print(a)
