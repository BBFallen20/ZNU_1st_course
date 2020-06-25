
def convertor(num, to_base=10, from_base=10):
	try:
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

print("="*50)
print("\t\tЛабораторная работа №4")
print("\t\tПоддубняк Д.")
print("="*50)
while True:
	print('''Выберите действие:
1.Начать работу
2.Выход''')
	what= input()
	if what == "1":
		try:
			from_system=int(input("Введите систему счисления вашего числа(2-16):"))
			if from_system>=2 and from_system<=16:
				pass
			else:
				print("Неверно введена система счисления.")
				break
		except ValueError:
			print("Неверно введена система счисления.")
			break
		try:
			system=int(input("Введите систему счисления для перевода(2-16):"))
			if system>=2 and system<=16:
				pass
			else:
				print("Неверно введена система счисления.")	
				break
		except ValueError:
			print("Неверно введена система счисления.")
			break
		number=input("Введите число для перевода:")
		print("В "+str(from_system)+"-ой системе счисления ваше число выглядит так:")
		print(convertor(number,system,from_system))
	elif what == "2":
		exit()
	else:
		print("Неверно выбрано действие.")	