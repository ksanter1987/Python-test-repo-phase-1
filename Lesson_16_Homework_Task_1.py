from calculations import addition
print('Welcome to the addition function')
try:
	number1 = float(input(f'Enter first value: '))
	number2 = float(input(f'Second value: '))
	if isinstance(number1, float) and isinstance(number2, float):
		result = addition(number1, number2)
		print(f'The value of your operation is {result}')
	else:
		raise ValueError

except ValueError as e:
	print('Please enter numbers')




import sys
print(sys.path)
sys.path.append("C:\\Users\\Ksanter\\Documents\\GitHub\\Python-test-repo-phase-1\\a\\b")
print(sys.path)
#from calculations import addition
sys.path.append("C:\\Users\\Ksanter\\Documents\\GitHub")
print(sys.path)
from calculations import addition
print(addition(2, 3))



