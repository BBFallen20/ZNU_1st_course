class Calculator:

    def __init__(self, first_digit, second_digit, mode):
        self.first_digit = str(first_digit)
        self.second_digit = str(second_digit)
        self.mode = mode
        self.solution = lambda x, y: x + y
        self.subtraction = lambda x, y: x - y
        self.multiplication = lambda x, y: x * y
        self.division = lambda x, y: x / y

    def typechecker(self, digit):
        if '.' in digit:
            try:
                return float(digit)
            except:
                return 'Error'
        else:
            try:
                return int(digit)
            except:
                return 'Error'

    def get_answer(self):
        checked_first = self.typechecker(self.first_digit)
        checked_second = self.typechecker(self.second_digit)
        if self.mode == '+':
            return self.solution(checked_first, checked_second)
        elif self.mode == '-':
            return self.subtraction(checked_first, checked_second)
        elif self.mode == '*':
            return self.multiplication(checked_first, checked_second)
        elif self.mode == '/':
            return self.division(checked_first, checked_second)
        else:
            return 'Unknown mode'

    def continued(self):
        self.first_digit = str(self.get_answer())
        self.mode = input("Enter mode(+,-,*,/):")
        self.second_digit = input("Enter second digit:")
        return self.get_answer()


a = Calculator(20, 10, "/")
print(a.get_answer())
print(a.continued())
