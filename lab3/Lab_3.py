import time

def binartodef(x):
	lenght=len(x)
	d=0
	for i in range(0,lenght):
		d=d+int(x[i])*(2**(lenght-i-1))
	print("В десятичном виде:")
	return d

def alphacheck(alphabet='01'): 				#функция сверки строки с алфавитом
	s = input("Введите строку: ").rstrip() 			#строка с клавиатуры
	if len(s) == 0: 								#проверка наличия ввода
		return "Пустая строка,попробуйте еще раз..."
	for i in s: 									#цикл перебора строки посимвольно
		if i in alphabet: 
			flag = True 							#если в строке только алфавит:присваивает значение правда
		else:
			flag = False 							#если в строке что-то помимо алфавита:присваивает значение ложь
			break 									#выход из цикла
			
	if flag: 										#сверка значений Правда-Ложь для вывода результата
		print ("В строке только цифры")
		return(binartodef(s))

	else:
		return "В строке обнаружены символы помимо цифр."

print("="*50)
print("\t\tЛабораторная работа №3")
print("\t\tПоддубняк Д.")
print("="*50)
while True: #цикл бесконечного вывода на экран
	time.sleep(1.5)
	print('\nЗавершить программу: "выход"')	#псевдоменю
	mode = input('Начать работу: "ENTER"\n')
	if mode == "выход":
		exit()
	print(alphacheck())	#вызов функции