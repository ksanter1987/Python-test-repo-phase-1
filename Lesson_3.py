# Lesson 3 Task 1
sample_string = 'helloworld'
if len(sample_string) >= 2:
	print(sample_string[0:2] + sample_string[-2:])
else:
	print()

#Lesson 3 Task 2
phone_number = '1234567890'
if phone_number.isdigit():
	if len(phone_number) == 10:
		print('This is a phone number')
	else:
		print("You are using wrong format of a phone number") 
else:
	print('This is not a phone number')


#Lesson 3 Task 3
name1 = 'oleksiy'
name2 = input('Введите имя: ')
if name2.isalpha():
	if name1.capitalize() == name2.capitalize():
		print(f'Hello {name1.capitalize()}')
	else:
		print('Wrong name!!!')
else:
	print('Wrong name format')