		
def add_contact(some_dict, some_list):
	first_name = input('Print first name: ')
	last_name = input('Print last name: ')
	full_name = first_name + ' ' + last_name
	phone = input('Print phone: ')
	city = input('Print city: ')
	new_entry = some_dict.copy()
	new_entry['first_name'] = first_name
	new_entry['last_name'] = last_name
	new_entry['full_name'] = full_name
	new_entry['phone'] = phone
	new_entry['city'] = city
	return some_list.append(new_entry)


def first_name_search(some_list):
	query = input('First name: ')
	for item in some_list:
		if item['first_name'] == query:
			print('Found person:')
			print(item)
			action = input("""What to do next:
			next - search next record
			menu - return to menu
			
			: """).strip().lower()
			if action == 'next':
				continue
			elif action == 'menu':
				break
		else:
			break

def last_name_search(some_list):
	query = input('Last name: ')
	for item in some_list:
		if item['last_name'] == query:
			print('Found person:')
			print(item)
			action = input("""What to do next:
			next - search next record
			menu - return to menu

			: """).strip().lower()
			if action == 'next':
				continue
			elif action == 'menu':
				break
		else:
			break


def full_name_search(some_list):
	query = input('Full name: ')
	for item in some_list:
		if item['full_name'] == query:
			print('Found person:')
			print(item)
			action = input("""What to do next:
			next - search next record
			menu - return to menu

			: """).strip().lower()
			if action == 'next':
				continue
			elif action == 'menu':
				break
		else:
			break



def phone_search(some_dict, some_list):
	query = input('Phone number: ')
	for item in some_list:
		if item['phone'] == query:
			print('Found person:')
			print(item)
			action = input("""What to do next:
			next - search next record
			update - update a record
			delete - delete a record
			menu - return to menu

			: """).strip().lower()
			if action == 'next':
				continue
			elif action == 'update':
				new_first_name = input('Enter new first name: ')
				new_last_name = input('Enter new last name: ')
				new_full_name = new_first_name + ' ' + new_last_name
				new_phone = input('Enter new phone number: ')
				new_city = input('Enter new city: ')
				item['first_name'] = new_first_name
				item['last_name'] = new_last_name
				item['full_name'] = new_full_name
				item['phone'] = new_phone
				item['city'] = new_city
				break
			elif action == 'delete':
				some_list.remove(item)
				break
			elif action == 'menu':
				break



def city_search(some_list):
	query = input('City: ')
	for item in some_list:
		if item['city'] == query:
			print('Found person:')
			print(item)
			action = input("""What to do next:
			next - search next record
			menu - return to menu

			: """).strip().lower()
			if action == 'next':
				continue
			elif action == 'menu':
				break
		else:
			break