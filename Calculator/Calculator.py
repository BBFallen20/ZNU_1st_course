class Calculator:
    solution = lambda x, y: x + y
    subtraction = lambda x, y: x - y
    multiplication = lambda x, y: x * y
    division = lambda x, y: x / y

    def __init__(self, first_digit, second_digit, mode):
        self.first_digit = first_digit
        self.second_digit = second_digit
        self.mode = mode

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
        if self.mode == '+':
            return self.typechecker(self.first_digit) + self.typechecker(self.second_digit)
        elif self.mode == '-':
            return self.typechecker(self.first_digit) - self.typechecker(self.second_digit)
        elif self.mode == '*':
            return self.typechecker(self.first_digit) * self.typechecker(self.second_digit)
        elif self.mode == '/':
            return self.typechecker(self.first_digit) / self.typechecker(self.second_digit)
        else:
            return 'Unknown mode'


