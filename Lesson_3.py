# Lesson 3 Task 1 (String manipulation)

# Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given string. If the string length is less than 2,
# return instead of the empty string.

sample_string = 'helloworld'
if len(sample_string) >= 2:
	print(sample_string[0:2] + sample_string[-2:])
else:
	print()
print()



# Lesson 3 Task 2 (The valid phone number program). Variant 1
# Make a program that checks if a string is in the right format 
# for a phone number. The program should check that the string 
# contains only numerical characters and is only 10 characters long. 
# Print a suitable message depending on the outcome of the string evaluation.

phone_number = '1234567890'
if phone_number.isdigit():
	if len(phone_number) == 10:
		print('This is a phone number')
	else:
		print("You are using wrong format of a phone number") 
else:
	print('This is not a phone number')
print()

# Lesson 3 Task 2 (The valid phone number program). Variant 2

phone_number = '1234567890'
if phone_number.isdigit() and len(phone_number) == 10:
	print('This is a phone number')
elif phone_number.isdigit() and len(phone_number) != 10:
	print("You are using wrong format of a phone number") 
else:
	print('This is not a phone number')
print()

#Lesson 3 Task 2 (The valid phone number program). Variant 3

phone_number = input('Введіть телефонний номер: +38')
if phone_number.isdigit() and len(phone_number) == 10:
	print('This is a phone number')
elif phone_number.isdigit() and len(phone_number) != 10:
	print("You are using wrong format of a phone number") 
else:
	print('This is not a phone number')
print()



# Lesson 3 Task 3 (The name check)
# Write a program that has a variable with your name stored (in lowercase)
# and then asks for your name as input. The program should check if your input 
# is equal to the stored name even if the given name has another case, e.g., 
# if your input is “Anton” and the stored name is “anton”, it should return True

name1 = 'oleksiy'
name2 = input('Введите имя: ')
if name2.isalpha():
	if name1.capitalize() == name2.capitalize():
		print(f'Hello {name1.capitalize()}')
	else:
		print('Wrong name!!!')
else:
	print('Wrong name format')
print()