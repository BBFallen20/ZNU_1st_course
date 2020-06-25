# Лабораторная работа №6
# Поддубняк Д.
# Функции: binarconverter = перевод из 10 СС в 2 СС, straight_code = перевод в прямой код, additinally_code = перевод в дополнительный код
# reverse_code = перевод в обратный код
# Переменные:decimal_digit = исходное число в 10 СС, straight_view = число в прямом коде, additinally_view = число в дополнительном коде
# reverse_view = число в обратном коде




def binarconverter(x,res=''): #перевод десятичного числа в двоичную СС.
    x = int(x)
    if x == 0:
        return '0'
    else:
    	while x > 0:
        	res = ('0' if x % 2 == 0 else '1') + res # Формула перевода в бинарный вид
        	x //= 2
    	return str(res)


def straight_code(num, ispositive='+'):
	l = len(num) # Длинна числа
	if ispositive == '-': # Если отрицательное:
		num = '1 '+('0'*(8-l-1))+num
	else:# Если положительное:
		num = '0 '+('0'*(8-l-1))+num
	return num


def additinally_code(n, bits=8):
	n = int(n)
	mask = (1 << bits) - 1 # Побитовый снос
	if n < 0:
		n = ((abs(n) ^ mask) + 1)
	answer = (binarconverter(n & mask)) # Перевод в 2 СС числа с бинарным операндом И
	answer = str(answer)
	return answer


def reverse_code(num):
	new_num = '' # Переменная для коррекции
	if num[0] == '0': # Инверсия путем добавления в переменную для коррекции итоговых значений
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
	return num_part+' '+new_num # Соединение итогового числа с разрядной цифрой

print("="*50)
print('''Лабораторная работа №6
Поддубняк Д.''')
print("="*50)
while True:
	try:
		decimal_digit = input("Введите число в десятичной СС(от -128 до 128):\n")
		if int(decimal_digit) <= 127 and int(decimal_digit) >= -127: # Ограничение числа(Конфигурабельно)
			if '-' in decimal_digit:# Если число отрицательное:
				split = decimal_digit.split('-')# Список для отделения минуса от числа
				split[0] = '-'# Отделение минуса
				binar_digit = (binarconverter(split[1]))
				straight_view = straight_code(binar_digit,split[0])
				reverse_view = reverse_code(straight_view)
				additinally_view = additinally_code(decimal_digit)
				print(f'''В двоичном виде: {binar_digit}
В прямом коде: {straight_view}
В обратном коде: {reverse_view}
В дополнительном коде: {additinally_view}
''')
			elif not '-' in decimal_digit:# Если число положительное:
				binar_digit = binarconverter(decimal_digit)
				straight_view = straight_code(binar_digit)
				reverse_view = straight_view
				additinally_view = straight_view
				print(f'''В двоичном виде: {binar_digit}
В прямом коде: {straight_view}
В обратном коде: {reverse_view}
В дополнительном коде: {additinally_view}
''')
		else:
			print("Система рассчитана на число меньше 128|болше -128")
			continue
	except Exception:
		print("Неверно введено число.")
		continue
