import json
import sys
from phonebook4_func import add_contact, first_name_search, last_name_search, full_name_search, phone_search, city_search


print(sys.argv)
if len(sys.argv) < 2:
    print('Please specify json file name')
    exit()
filename = sys.argv[1]
json_file = open(filename)
try:
	phonebook = json.load(json_file)
except json.decoder.JSONDecodeError:
	phonebook = []

json_file.close()
dict_pattern = {
	'first_name': '',
	'last_name': '',
	'full_name': '',
	'phone': '',
	'city': ''
}
try:
	while True:
		command = input('''Select command from the list: 
			add - to add new contact
			search - to find a contact
			exit - to exit the phonebook
			: ''').strip().lower()
		if command == 'add':
			add_contact(dict_pattern, phonebook)
		elif command == 'search':
			while True:
				search_method = input('''choose a search method:
					1. search by first name
					2. search by last name
					3. search by full name
					4. search by phone number
					5. search by city
					6. return to main menu
					 ''')
				if search_method == '1':
					first_name_search(phonebook)
				elif search_method == '2':
					last_name_search(phonebook)
				elif search_method == '3':
					full_name_search(phonebook)
				elif search_method == '4':
					phone_search(dict_pattern, phonebook)
				elif search_method == '5':
					city_search(phonebook)
				elif search_method == '6':
					break
				else:
					continue
		elif command == 'exit':
			print('Thx for using phonebook!')
			break
except Exception as e:
	print('Unexpected error')
	print(e)
finally:
	with open(filename, 'w') as json_file:
		json.dump(phonebook, json_file, indent=4)	