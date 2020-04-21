import random
print()
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
				12. ручне введення операцій
				13. вийти з програми


				""")
			operation = operation.strip()
			print()
			if operation.isdigit() and operation == '1':
				print('Проводимо операцію додавання')
				while True:
					number1 = input('Введіть перше число: ')
					number1 = number1.strip()
					if number1[0:].isdigit():
						number1 = float(number1)
						break
					elif number1[0] == '-' and number1[1:].isdigit():
						number1 = float(number1)
						break
					elif number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[0:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
						number1 = float(number1)
						break
					elif number1[0] == '-' and number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[1:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
						number1 = float(number1)
						break
					else:
						continue
				while True:
					number2 = input('Введіть друге число: ')
					number2 = number2.strip()
					if number2[0:].isdigit():
						number2 = float(number2)
						break
					elif number2[0] == '-' and number2[1:].isdigit():
						number2 = float(number2)
						break
					elif number2[1:len(number2)-1].find('.') == number2[1:len(number2)-1].rfind('.') and number2[0:number2.find('.')].isdigit() and number2[number2.find('.')+1:].isdigit():
						number2 = float(number2)
						break
					elif number2[0] == '-' and number2[1:len(number2)-1].find('.') == number2[1:len(number2)-1].rfind('.') and number2[1:number2.find('.')].isdigit() and number2[number2.find('.')+1:].isdigit():
						number2 = float(number2)
						break
					else:
						continue
				print()
				print(f'Результат додавання: {number1} + {number2} = {number1 + number2}')
				print()
			elif operation.isdigit() and operation == '2':
				print('Проводимо операцію віднімання')
				while True:
					number1 = input('Введіть перше число: ')
					number1 = number1.strip()
					if number1[0:].isdigit():
						number1 = float(number1)
						break
					elif number1[0] == '-' and number1[1:].isdigit():
						number1 = float(number1)
						break
					elif number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[0:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
						number1 = float(number1)
						break
					elif number1[0] == '-' and number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[1:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
						number1 = float(number1)
						break
					else:
						continue
				while True:
					number2 = input('Введіть друге число: ')
					number2 = number2.strip()
					if number2[0:].isdigit():
						number2 = float(number2)
						break
					elif number2[0] == '-' and number2[1:].isdigit():
						number2 = float(number2)
						break
					elif number2[1:len(number2)-1].find('.') == number2[1:len(number2)-1].rfind('.') and number2[0:number2.find('.')].isdigit() and number2[number2.find('.')+1:].isdigit():
						number2 = float(number2)
						break
					elif number2[0] == '-' and number2[1:len(number2)-1].find('.') == number2[1:len(number2)-1].rfind('.') and number2[1:number2.find('.')].isdigit() and number2[number2.find('.')+1:].isdigit():
						number2 = float(number2)
						break
					else:
						continue
				print()
				print(f'Результат віднімання: {number1} - {number2} = {number1 - number2}')
				print()
			elif operation.isdigit() and operation == '3':
				print('Проводимо операцію множення')
				while True:
					number1 = input('Введіть перше число: ')
					number1 = number1.strip()
					if number1[0:].isdigit():
						number1 = float(number1)
						break
					elif number1[0] == '-' and number1[1:].isdigit():
						number1 = float(number1)
						break
					elif number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[0:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
						number1 = float(number1)
						break
					elif number1[0] == '-' and number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[1:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
						number1 = float(number1)
						break
					else:
						continue
				while True:
					number2 = input('Введіть друге число: ')
					number2 = number2.strip()
					if number2[0:].isdigit():
						number2 = float(number2)
						break
					elif number2[0] == '-' and number2[1:].isdigit():
						number2 = float(number2)
						break
					elif number2[1:len(number2)-1].find('.') == number2[1:len(number2)-1].rfind('.') and number2[0:number2.find('.')].isdigit() and number2[number2.find('.')+1:].isdigit():
						number2 = float(number2)
						break
					elif number2[0] == '-' and number2[1:len(number2)-1].find('.') == number2[1:len(number2)-1].rfind('.') and number2[1:number2.find('.')].isdigit() and number2[number2.find('.')+1:].isdigit():
						number2 = float(number2)
						break
					else:
						continue
				print()
				print(f'Результат множення: {number1} * {number2} = {number1 * number2}')
				print()
			elif operation.isdigit() and operation == '4':
				print('Проводимо операцію ділення')
				while True:
					number1 = input('Введіть перше число: ')
					number1 = number1.strip()
					if number1[0:].isdigit():
						number1 = float(number1)
						break
					elif number1[0] == '-' and number1[1:].isdigit():
						number1 = float(number1)
						break
					elif number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[0:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
						number1 = float(number1)
						break
					elif number1[0] == '-' and number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[1:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
						number1 = float(number1)
						break
					else:
						continue
				while True:
					number2 = input('Введіть друге число: ')
					number2 = number2.strip()
					if number2[0:].isdigit():
						number2 = float(number2)
						if number2 != 0:
							break
						else:
							continue
					elif number2[0] == '-' and number2[1:].isdigit():
						number2 = float(number2)
						if number2 != 0:
							break
						else:
							continue						
					elif number2[1:len(number2)-1].find('.') == number2[1:len(number2)-1].rfind('.') and number2[0:number2.find('.')].isdigit() and number2[number2.find('.')+1:].isdigit():
						number2 = float(number2)
						if number2 != 0:
							break
						else:
							continue						
					elif number2[0] == '-' and number2[1:len(number2)-1].find('.') == number2[1:len(number2)-1].rfind('.') and number2[1:number2.find('.')].isdigit() and number2[number2.find('.')+1:].isdigit():
						number2 = float(number2)
						if number2 != 0:
							break
						else:
							continue						
					else:
						continue
				print()
				print(f'Результат ділення: {number1} / {number2} = {number1 / number2}')
				print()
			elif operation.isdigit() and operation == '5':
				print('Проводимо операцію ділення націло')
				while True:
					number1 = input('Введіть перше число: ')
					number1 = number1.strip()
					if number1[0:].isdigit():
						number1 = float(number1)
						break
					elif number1[0] == '-' and number1[1:].isdigit():
						number1 = float(number1)
						break
					elif number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[0:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
						number1 = float(number1)
						break
					elif number1[0] == '-' and number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[1:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
						number1 = float(number1)
						break
					else:
						continue
				while True:
					number2 = input('Введіть друге число: ')
					number2 = number2.strip()
					if number2[0:].isdigit():
						number2 = float(number2)
						if number2 != 0:
							break
						else:
							continue						
					elif number2[0] == '-' and number2[1:].isdigit():
						number2 = float(number2)
						if number2 != 0:
							break
						else:
							continue						
					elif number2[1:len(number2)-1].find('.') == number2[1:len(number2)-1].rfind('.') and number2[0:number2.find('.')].isdigit() and number2[number2.find('.')+1:].isdigit():
						number2 = float(number2)
						if number2 != 0:
							break
						else:
							continue						
					elif number2[0] == '-' and number2[1:len(number2)-1].find('.') == number2[1:len(number2)-1].rfind('.') and number2[1:number2.find('.')].isdigit() and number2[number2.find('.')+1:].isdigit():
						number2 = float(number2)
						if number2 != 0:
							break
						else:
							continue						
					else:
						continue
				print()
				print(f'Результат ділення націло: {number1} // {number2} = {number1 // number2}')
				print()
			elif operation.isdigit() and operation == '6':
				print('Проводимо операцію визначення остачі від цілочисленного ділення')
				while True:
					number1 = input('Введіть перше число: ')
					number1 = number1.strip()
					if number1[0:].isdigit():
						number1 = float(number1)
						break
					elif number1[0] == '-' and number1[1:].isdigit():
						number1 = float(number1)
						break
					elif number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[0:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
						number1 = float(number1)
						break
					elif number1[0] == '-' and number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[1:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
						number1 = float(number1)
						break
					else:
						continue
				while True:
					number2 = input('Введіть друге число: ')
					number2 = number2.strip()
					if number2[0:].isdigit():
						number2 = float(number2)
						if number2 != 0:
							break
						else:
							continue						
					elif number2[0] == '-' and number2[1:].isdigit():
						number2 = float(number2)
						if number2 != 0:
							break
						else:
							continue						
					elif number2[1:len(number2)-1].find('.') == number2[1:len(number2)-1].rfind('.') and number2[0:number2.find('.')].isdigit() and number2[number2.find('.')+1:].isdigit():
						number2 = float(number2)
						if number2 != 0:
							break
						else:
							continue						
					elif number2[0] == '-' and number2[1:len(number2)-1].find('.') == number2[1:len(number2)-1].rfind('.') and number2[1:number2.find('.')].isdigit() and number2[number2.find('.')+1:].isdigit():
						number2 = float(number2)
						if number2 != 0:
							break
						else:
							continue						
					else:
						continue
				print()
				print(f'Остача від цілочисленного ділення: {number1} % {number2} = {number1 % number2}')
				print()
			elif operation.isdigit() and operation == '7':
				print('Проводимо операцію піднесення числа до степеня')
				while True:
					number1 = input('Введіть основу степеня: ')
					number1 = number1.strip()
					if number1[0:].isdigit():
						number1 = float(number1)
						break
					elif number1[0] == '-' and number1[1:].isdigit():
						number1 = float(number1)
						break
					elif number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[0:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
						number1 = float(number1)
						break
					elif number1[0] == '-' and number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[1:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
						number1 = float(number1)
						break
					else:
						continue
				while True:
					number2 = input('Введіть показник степеня: ')
					number2 = number2.strip()
					if number2[0:].isdigit():
						number2 = float(number2)
						break
					elif number2[0] == '-' and number2[1:].isdigit():
						number2 = float(number2)
						break
					elif number2[1:len(number2)-1].find('.') == number2[1:len(number2)-1].rfind('.') and number2[0:number2.find('.')].isdigit() and number2[number2.find('.')+1:].isdigit():
						number2 = float(number2)
						break
					elif number2[0] == '-' and number2[1:len(number2)-1].find('.') == number2[1:len(number2)-1].rfind('.') and number2[1:number2.find('.')].isdigit() and number2[number2.find('.')+1:].isdigit():
						number2 = float(number2)
						break
					else:
						continue
				print()
				print(f'Результат піднесення числа {number1} до степеню {number2} = {number1 ** number2}')
				print()
			elif operation.isdigit() and operation == '8':
				print('Проводимо операцію округлення числа')
				while True:
					number1 = input('Введіть число для округлення: ')
					number1 = number1.strip()
					if number1[0:].isdigit():
						number1 = float(number1)
						break
					elif number1[0] == '-' and number1[1:].isdigit():
						number1 = float(number1)
						break
					elif number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[0:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
						number1 = float(number1)
						break
					elif number1[0] == '-' and number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[1:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
						number1 = float(number1)
						break
					else:
						continue
				number2 = round(number1)
				print()
				print(f'Результатом округлення числа {number1} є {number2}')
				print()
			elif operation.isdigit() and operation == '9':
				print('Проводимо операцію видобування кореня n-ї степені з числа')
				while True:
					number1 = input('Введіть число з якого хочете добути корінь: ')
					number1 = number1.strip()
					if number1[0:].isdigit():
						number1 = float(number1)
						break
					elif number1[0] == '-' and number1[1:].isdigit():
						number1 = float(number1)
						break
					elif number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[0:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
						number1 = float(number1)
						break
					elif number1[0] == '-' and number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[1:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
						number1 = float(number1)
						break
					else:
						continue
				while True:
					number2 = input('Введіть степінь кореня ')
					number2 = number2.strip()
					if number2[0:].isdigit():
						number2 = float(number2)
						break
					elif number2[0] == '-' and number2[1:].isdigit():
						number2 = float(number2)
						break
					elif number2[1:len(number2)-1].find('.') == number2[1:len(number2)-1].rfind('.') and number2[0:number2.find('.')].isdigit() and number2[number2.find('.')+1:].isdigit():
						number2 = float(number2)
						break
					elif number2[0] == '-' and number2[1:len(number2)-1].find('.') == number2[1:len(number2)-1].rfind('.') and number2[1:number2.find('.')].isdigit() and number2[number2.find('.')+1:].isdigit():
						number2 = float(number2)
						break
					else:
						continue 
				print()
				print(f'Корінь {number2}-ї степені з числа {number1} = {number1 ** (1 / number2)}')
				print()
			elif operation.isdigit() and operation == '10':
				print('Проводимо операцію визначення факторіала числа')
				while True:
					number1 = input("Введіть ціле невід'ємне число, з якого хочете визначити факторіал: ")
					number1 = number1.strip()
					if number1.isdigit():
						number1 = int(number1)
						break
					elif number1 == '0':
						number1 = 1
						break
					else:
						continue
				n = 1
				factorial = 1
				while True:
					factorial *= n
					n += 1
					if n > number1:
						break
				print()
				print(f'Факторіал числа {number1} = {factorial}')
				print()
			elif operation.isdigit() and operation == '11':
				print('Виводимо випадкове ціле число в діапазоні')
				while True:
					while True:
						number1 = input('Введіть нижню границю діапазону: ')
						number1 = number1.strip()
						if number1[0:].isdigit():
							number1 = int(number1)
							break
						elif number1[0] == '-' and number1[1:].isdigit():
							number1 = int(number1)
							break
						elif number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[0:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
							number1 = round(float(number1))
							break
						elif number1[0] == '-' and number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[1:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
							number1 = round(float(number1))
							break
						else:
							continue
					while True:
						number2 = input('Введіть верхню границю діапазону: ')
						number2 = number2.strip()
						if number2[0:].isdigit():
							number2 = int(number2)
							break
						elif number2[0] == '-' and number2[1:].isdigit():
							number2 = int(number2)
							break
						elif number2[1:len(number2)-1].find('.') == number2[1:len(number2)-1].rfind('.') and number2[0:number2.find('.')].isdigit() and number2[number2.find('.')+1:].isdigit():
							number2 = round(float(number2))
							break
						elif number2[0] == '-' and number2[1:len(number2)-1].find('.') == number2[1:len(number2)-1].rfind('.') and number2[1:number2.find('.')].isdigit() and number2[number2.find('.')+1:].isdigit():
							number2 = round(float(number2))
							break
						else:
							continue
					if number2 > number1:
						print()
						print(f'Випадкове число в діапазоні від {number1} до {number2} = {random.randint(number1, number2)}')
						break
					else:
						continue
				print()
			elif operation.isdigit() and operation == '12':
				while True:
					command = input(f"""Введіть математичне рівняння розмеживши знак операції з числами пробілом:
					
				  додавання '+'
				  віднімання '-'
				  множення '*'
				  ділення '/'
				  ділення націло '//'
				  остача від цілочисельного ділення 'mod'
				  піднести число в степінь '**'
				  визначення корення n-ї степені з числа 'sqrt'
				  вихід з розділу 'exit'


				""")
					command = command.strip()
					print()
					if command == 'exit':
						break
					text = command.split()
					if len(text) >= 3:
						number1 = text[0]
						if number1[0:].isdigit():
							number1 = float(number1)
						elif number1[0] == '-' and number1[1:].isdigit():
							number1 = float(number1)
						elif number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[0:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
							number1 = float(number1)
						elif number1[0] == '-' and number1[1:len(number1)-1].find('.') == number1[1:len(number1)-1].rfind('.') and number1[1:number1.find('.')].isdigit() and number1[number1.find('.')+1:].isdigit():
							number1 = float(number1)
						else:
							continue
						number2 = text[2]
						if number2[0:].isdigit():
							number2 = float(number2)
						elif number2[0] == '-' and number2[1:].isdigit():
							number2 = float(number2)
						elif number2[1:len(number2)-1].find('.') == number2[1:len(number2)-1].rfind('.') and number2[0:number2.find('.')].isdigit() and number2[number2.find('.')+1:].isdigit():
							number2 = float(number2)
						elif number2[0] == '-' and number2[1:len(number2)-1].find('.') == number2[1:len(number2)-1].rfind('.') and number2[1:number2.find('.')].isdigit() and number2[number2.find('.')+1:].isdigit():
							number2 = float(number2)
						else:
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
					else:
						continue
					
			if operation.isdigit() and operation == '13':
				break

			else:
				continue

		print(f'Дякуємо {user_name} за використання калькулятора')
		break
	else:
		print("Будь-ласка, введіть своє ім'я правильно")
		continue


