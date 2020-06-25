# Сложение(вычитание) чисел в дополнительном коде
# Поддубняк Д. 6.1219-2
# Функции: __init__ = конструктор класса,обьявляет переменные, binarconverter = конвертор в двоичный вид,
# straight_code = перевод в прямой код, reverse_code = перевод в обратный код, additionally_code = перевод в
# дополнительный код, solution, substraction = сложение,вычитание
#
# Объявляем класс "Числа"
class Digits:
    def __init__(self, first_num, second_num, mode=None):
        self.mode = mode # Сложение или вычитание
        self.first_num = first_num # Первое число
        self.second_num = second_num # Второе число
        self.converted_first = self.binarconverter(self.first_num) # Первое в двоичном виде
        self.converted_second = self.binarconverter(self.second_num) # Второе в двоичном виде
        self.straight_first = self.straight_code(self.converted_first, first_num) # Первое в прямом коде
        self.straight_second = self.straight_code(self.converted_second, second_num) # Второе в прямом коде
        if int(first_num) > 0: # Если первое положительное
            self.reversed_first = self.straight_first # Обратный код равен прямому
            self.additionally_first = self.straight_first # Дополнительный код равен прямому
        else: # Иначе:
            self.reversed_first = self.reverse_code(self.straight_first) # Функция перевода в обратный код
            self.additionally_first = self.additionally_code(str(self.first_num)) # Функция перевода в доп.код
        if int(second_num) > 0: # Если второе положительое
            self.reversed_second = self.straight_second # Обратный код равен прямому
            self.additionally_second = self.straight_second # Дополнительный код равен прямому
        else: # Иначе:
            self.reversed_second = self.reverse_code(self.straight_second) # Функция перевода в обратный код
            self.additionally_second = self.additionally_code(str(self.second_num)) # Функция перевода в доп.код
        if self.mode == "+": # Если + то сложение
            self.solution_result = self.solution(self.additionally_first, self.additionally_second) # Функция сложения
        elif self.mode == "-": # Если - вычитание
            self.subtraction_result = self.subtraction() # Функция вычитания

    def binarconverter(self, x, res=''):  # перевод десятичного числа в двоичную СС.
        x = str(x)
        if '-' in x:
            x1 = '-'
            x = int(x.replace('-', ''))
            if x == 0:
                return '0'
            else:
                while x > 0:
                    res = ('0' if x % 2 == 0 else '1') + res  # Формула перевода в бинарный вид
                    x //= 2
                return str(res)
        else:
            x = int(x)
            if x == 0:
                return '0'
            else:
                while x > 0:
                    res = ('0' if x % 2 == 0 else '1') + res  # Формула перевода в бинарный вид
                    x //= 2
                return str(res)

    def straight_code(self, num, ispositive):
        l = len(num)  # Длинна числа
        if '-' in ispositive:  # Если отрицательное:
            num = '1' + ('0' * (8 - l - 1)) + num
        else:  # Если положительное:
            num = '0' + ('0' * (8 - l - 1)) + num
        return num

    def reverse_code(self, num):
        new_num = ''  # Переменная для коррекции
        num_part = ''
        if num[0] == '0':  # Инверсия путем добавления в переменную для коррекции итоговых значений
            num_part = num[0] + ''
            num = num[1:]
        elif num[0] == '1':
            num_part = num[0] + ''
            num = num[1:]
        for i in range(len(num)):
            if num[i] == '0':
                new_num += '1'
            elif num[i] == '1':
                new_num += '0'
        return num_part + new_num  # Соединение итогового числа с разрядной цифрой

    def additionally_code(self, n, bits=8):
        n = int(n)
        mask = (1 << bits) - 1  # Побитовый снос
        if n < 0:
            n = ((abs(n) ^ mask) + 1)
        answer = (self.binarconverter(n & mask))  # Перевод в 2 СС числа с бинарным операндом И
        answer = str(answer)
        return answer

    def solution(self, num1, num2):
        result = list()  # Пустой список для записи результата сложения
        p = 0  # Вспомогательная переменная для сложения (перенос единицы)
        a = list(map(int, num1[:]))  # Перевод всех чисел в списке в int
        b = list(map(int, num2[:]))  # Перевод всех чисел в списке в int

        # Прохождение циклом в обратном порядке (от -1 до -7 (индексы в списке))
        for i in range(-1, -8, -1):
            if (a[i] + b[i] + p) == 0:
                result.append('0')
                p = 0
            elif (a[i] + b[i] + p) == 1:
                result.append('1')
                p = 0
            elif (a[i] + b[i] + p) == 2:
                result.append('0')
                p = 1
            elif (a[i] + b[i] + p) == 3:
                result.append('1')
                p = 1
        return "".join(result[::-1])

    def subtraction(self):
        ready_digit = '-' + self.second_num # Меняет знак второму числу на отрицательный
        additionally_digit = self.additionally_code(ready_digit) # Доп.код второго числа(уже отрицательного)
        return self.solution(self.additionally_first, additionally_digit) # Сложение первого числа и отрицательного второго


alphabet = '0123456789'
a = input("Enter first digit:\n")
b = input("Enter second digit:\n")
mode = input("Enter mode(+,-):\n")
for i in a:
    if i in alphabet:
        Flag = True
    else:
        Flag = False
for j in b:
    if j in alphabet:
        Flag = True
    else:
        Flag = False
if Flag:
    ex = Digits(a, b, mode) # Инициализирую экземпляр класса(первое и второе число)
    try:
        if mode == '+':
            print(ex.solution_result) # Вывожу результат
        elif mode == '-':
            print(ex.subtraction_result)
        else:
            print("Unknown mode.")
    except AttributeError:
        print("Error")
else:
    print("Error")
