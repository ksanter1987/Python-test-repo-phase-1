import random
import math
def positive_integer_value(value):
    if value.isdigit():
        return True
def negative_integer_value(value):
    if value[0] == '-' and value[1:].isdigit():
        return True
def positive_float_value(value):
    if '.' in value[1:-1] and value[1:-1].find('.') == value[1:-1].rfind('.') and value[0:value.find('.')].isdigit() and value[value.find('.')+1:].isdigit():
        return True
def negative_float_value(value):
    if value[0] == '-' and '.' in value[2:-1] and value[2:-1].find('.') == value[2:-1].rfind('.') and value[1:value.find('.')].isdigit() and value[value.find('.')+1:].isdigit():
        return True
def check_and_convert(value):
    if positive_integer_value(value) == True:
        return int(value)
    if negative_integer_value(value) == True:
        return int(value)
    if positive_float_value(value) == True:
        return float(value)
    if negative_float_value(value) == True:
        return float(value)
    else:
        return None
def manual_input(value1, value2):
	number1 = value1.strip()
	number2 = value2.strip()
	number1 = check_and_convert(value1)
	number2 = check_and_convert(value2)
	return number1, number2
while True:
	user_name = input("Будь-ласка, введіть своє ім'я: ")
	user_name = user_name.strip()
	user_name = user_name.capitalize()
	print()
	if user_name.isalpha():
		print(f'Вітаємо Вас в калькуляторі {user_name}')
		print()
		while True:
			operation = input(f"""{user_name} виберіть операцію зі списку наступних:
				1.  додавання 
				2.  віднімання
				3.  множення
				4.  ділення
				5.  ділення націло
				6.  остача від цілочисельного ділення
				7.  піднести число в степінь
				8.  округлити число
				9.  визначення корення n-ї степені з числа
				10. знайти факторіал числа
				11. вивести випадкове ціле число в діапазоні
				12. СПЕЦІАЛЬНИЙ РЕЖИМ (ручне введення операцій)
				13. вийти з програми


				""")
			operation = operation.strip()
			print()
			if operation.isdigit() and operation == '1':
				print('Проводимо операцію додавання')
				number1 = input('Введіть перше число: ')
				number2 = input('Введіть друге число: ')
				number1, number2 = manual_input(number1, number2)
				if number1 == None or number2 == None:
					print('Невірно внесені дані. Спробуйте ще раз.')
					continue
				else:
					print(f'Результат додавання: {number1} + {number2} = {number1 + number2}')
					print()
			elif operation.isdigit() and operation == '2':
				print('Проводимо операцію віднімання')
				number1 = input('Введіть перше число: ')
				number2 = input('Введіть друге число: ')
				number1, number2 = manual_input(number1, number2)
				if number1 == None or number2 == None:
					print('Невірно внесені дані. Спробуйте ще раз.')
					continue
				else:
					print(f'Результат віднімання: {number1} - {number2} = {number1 - number2}')
					print()
			elif  operation.isdigit() and operation == '3':
				print('Проводимо операцію множення')
				number1 = input('Введіть перше число: ')
				number2 = input('Введіть друге число: ')
				number1, number2 = manual_input(number1, number2)
				if number1 == None or number2 == None:
					print('Невірно внесені дані. Спробуйте ще раз.')
					continue
				else:
					print(f'Результат множення: {number1} * {number2} = {number1 * number2}')
					print()		
			elif  operation.isdigit() and operation == '4':
				print('Проводимо операцію ділення')
				number1 = input('Введіть перше число: ')
				number2 = input('Введіть друге число: ')
				number1, number2 = manual_input(number1, number2)
				if number1 == None or number2 == None or number2 == 0:
					print('Невірно внесені дані. Спробуйте ще раз.')
					continue
				else:
					print(f'Результат ділення: {number1} / {number2} = {number1 / number2}')
					print()
			elif  operation.isdigit() and operation == '5':
				print('Проводимо операцію ділення націло')
				number1 = input('Введіть перше число: ')
				number2 = input('Введіть друге число: ')
				number1, number2 = manual_input(number1, number2)
				if number1 == None or number2 == None or number2 == 0:
					print('Невірно внесені дані. Спробуйте ще раз.')
					continue
				else:
					print(f'Результат ділення націло: {number1} // {number2} = {number1 // number2}')
					print()
			elif  operation.isdigit() and operation == '6':
				print('Проводимо операцію визначення остачі від цілочисленного ділення')
				number1 = input('Введіть перше число: ')
				number2 = input('Введіть друге число: ')
				number1, number2 = manual_input(number1, number2)
				if number1 == None or number2 == None or number2 == 0:
					print('Невірно внесені дані. Спробуйте ще раз.')
					continue
				else:
					print(f'Остача від цілочисленного ділення: {number1} mod {number2} = {number1 % number2}')
					print()
			elif  operation.isdigit() and operation == '7':
				print('Проводимо операцію піднесення числа до степеня')
				number1 = input('Введіть основу степеня: ')
				number2 = input('Введіть показник степеня: ')
				number1, number2 = manual_input(number1, number2)
				if number1 == None or number2 == None:
					print('Невірно внесені дані. Спробуйте ще раз.')
					continue
				else:
					print(f'Результат піднесення числа {number1} до степеню {number2} = {number1 ** number2}')
					print()
			elif  operation.isdigit() and operation == '8':
				print('Проводимо операцію округлення числа')
				number1 = input('Введіть число для округлення: ')
				number1 = number1.strip()
				number1 = check_and_convert(number1)
				if number1 == None:
					print('Невірно внесені дані. Спробуйте ще раз.')
					continue										
				else:
					number2 = round(number1)
				print()
				print(f'Результатом округлення числа {number1} є {number2}')
				print()
			elif  operation.isdigit() and operation == '9':
				print('Проводимо операцію видобування кореня n-ї степені з числа')
				number1 = input('Введіть число з якого хочете добути корінь: ')
				number2 = input('Введіть степінь кореня: ')
				number1, number2 = manual_input(number1, number2)
				if number1 == None or number2 == None:
					print('Невірно внесені дані. Спробуйте ще раз.')
					continue
				else:
					print(f'Корінь {number2}-ї степені з числа {number1} = {number1 ** (1 / number2)}')
				print()
			elif  operation.isdigit() and operation == '10':
				print('Проводимо операцію визначення факторіала числа')
				number1 = input("Введіть ціле невід'ємне число, з якого хочете визначити факторіал: ")
				number1 = number1.strip()
				number1 = check_and_convert(number1)
				if number1 == None or number1 < 0 or str(number1).isdigit() != True:
					print('Невірно внесені дані. Спробуйте ще раз.')
					continue
				else:
					print(f'Факторіал числа {number1} = {math.factorial(number1)}')
			elif  operation.isdigit() and operation == '11':
				print('Виводимо випадкове ціле число в діапазоні')
				number1 = input('Введіть нижню границю діапазону: ')
				number2 = input('Введіть верхню границю діапазону: ')
				number1, number2 = manual_input(number1, number2)
				number1 = round(number1)
				number2 = round(number2)
				if number1 == None or number2 == None:
					print('Невірно внесені дані. Спробуйте ще раз.')
					continue
				elif number2 > number1:
					print(f'Випадкове число в діапазоні від {number1} до {number2} = {random.randint(number1, number2)}')
					print()				
				else:
					continue
			elif operation.isdigit() and operation == '12':
				operation_dict = {'+': 'Додавання двух чисел', '-': 'Віднімання двух чисел','*': 'Множення двух чисел','/': 'Ділення двух чисел','//': 'Ділення націло двух чисел','mod': 'Остача від цілочисленного ділення двух чисел','**': 'Піднесення до степеню','sqrt': 'корінь з числа','random': 'випадкове ціле число в діапазоні', 'exit': 'вихід з режиму'}
				for key, value in operation_dict.items():
					print(key, '-', value)
				print()
				while True:
					command = input('Введіть математичне рівняння розмеживши знак операції з числами пробілом: ')
					command = command.strip()
					if command == 'exit':
						break
					text = command.split()
					if len(text) == 3:
						number1 = text[0]
						number2 = text[2]
						number1, number2 = manual_input(number1, number2)
						if number1 == None or number2 == None:
							print('Невірно внесені дані. Спробуйте ще раз.')
							continue
					else:
						print('Введіть математичне рівняння у визначеному форматі')
						continue
					if text[1] == '+':
						print(f'{number1} + {number2} = {number1 + number2}')
					elif text[1] == '-':
						print(f'{number1} - {number2} = {number1 - number2}')
					elif text[1] == '*':
						print(f'{number1} * {number2} = {number1 * number2}')
					elif text[1] == '/' and number2 != 0:
						print(f'{number1} / {number2} = {number1 / number2}')
					elif text[1] == '//' and number2 != 0:
						print(f'{number1} // {number2} = {number1 // number2}')
					elif text[1] == 'mod' and number2 != 0:
						print(f'{number1} mod {number2} = {number1 % number2}')
					elif text[1] == '**':
						print(f'{number1} ** {number2} = {number1 ** number2}')
					elif text[1] == 'sqrt':
						print(f'{number1} sqrt {number2} = {number1 ** (1 / number2)}')
					elif text[1] == 'random' and number2 > number1:
						print(f'Випадкове число в діапазоні від {number1} до {number2} = {random.randint(number1, number2)}')
					else:
						continue
			elif  operation.isdigit() and operation == '13':
				break		
			else:
				continue
		print(f'Дякуємо {user_name} за використання калькулятора')
		break
	else:
		print("Будь-ласка, введіть своє ім'я правильно!")
		continue