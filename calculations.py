import random
import math
def addition(value1, value2):
	print('Проводимо операцію додавання')
	result = value1 + value2
	return result

def subtraction(value1, value2):
	print('Проводимо операцію віднімання')
	result = value1 - value2
	return result	

def multiplication(value1, value2):
	print('Проводимо операцію множення')
	result = value1 * value2
	return result	

def division(value1, value2):
	print('Проводимо операцію ділення')
	result = value1 / value2
	return result

def integer_division(value1, value2):
	print('Проводимо операцію цілочисленного ділення')
	result = value1 // value2
	return result

def modulo(value1, value2):
	print('Проводимо визначення остачі від ділення націло')
	result = value1 % value2
	return result

def power(value1, value2 = 2):
	print('Проводимо операцію піднесення до степеню')
	result = value1 ** value2
	return result

def sqrt(value1, value2 = 2):
	print('Проводимо операцію визначення кореня')
	if value2 != 0:
		result = value1 ** (1 / value2)
		return result
	else:
		print('На нуль ділити не можна')

def factor(value1):
	print('Проводимо операцію визначення факторіала')
	result = math.factorial(int(value1))
	return result

def random_number(value1, value2):
	print('Виводимо випадкове ціле число в діапазоні')
	if value2 > value1:
		result = random.randint(int(value1), int(value2))
		return result
		
def round_number(value1):
	print('Проводимо операцію округлення числа')
	result = round(value1)
	return result

def error_text():
	print('Неправильно введене значення', '\n')
	
