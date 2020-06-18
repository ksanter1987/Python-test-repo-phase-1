def add_contact(some_dict, some_list) -> list:
    first_name: str = input('Print first name: ')
    last_name: str = input('Print last name: ')
    full_name: str = first_name + ' ' + last_name
    phone: str = input('Print phone: ')
    city: str = input('Print city: ')
    new_entry: dict = some_dict.copy()
    new_entry['first_name'] = first_name
    new_entry['last_name'] = last_name
    new_entry['full_name'] = full_name
    new_entry['phone'] = phone
    new_entry['city'] = city
    return some_list.append(new_entry)


def first_name_search(some_list) -> str:
    query: str = input('First name: ')
    for item in some_list:
        if item['first_name'] == query:
            print('Found person:')
            print(item)
            action: str = input("""What to do next:
			next - search next record
			menu - return to menu
			
			: """).strip().lower()
            if action == 'next':
                continue
            elif action == 'menu':
                break
    return None


def last_name_search(some_list) -> str:
    query: str = input('Last name: ')
    for item in some_list:
        if item['last_name'] == query:
            print('Found person:')
            print(item)
            action: str = input("""What to do next:
			next - search next record
			menu - return to menu
			: """).strip().lower()
            if action == 'next':
                continue
            elif action == 'menu':
                break
    return None


def full_name_search(some_list) -> str:
    query: str = input('Full name: ')
    for item in some_list:
        if item['full_name'] == query:
            print('Found person:')
            print(item)
            action: str = input("""What to do next:
			next - search next record
			menu - return to menu
			: """).strip().lower()
            if action == 'next':
                continue
            elif action == 'menu':
                break
    return None


def phone_search(some_dict, some_list) -> str:
    query: str = input('Phone number: ')
    for item in some_list:
        if item['phone'] == query:
            print('Found person:')
            print(item)
            action: str = input("""What to do next:
			next - search next record
			update - update a record
			delete - delete a record
			menu - return to menu
			: """).strip().lower()
            if action == 'next':
                continue
            elif action == 'update':
                new_first_name: str = input('Enter new first name: ')
                new_last_name: str = input('Enter new last name: ')
                new_full_name = new_first_name + ' ' + new_last_name
                new_phone: str = input('Enter new phone number: ')
                new_city: str = input('Enter new city: ')
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
    return None


def city_search(some_list) -> str:
    query: str = input('City: ')
    for item in some_list:
        if item['city'] == query:
            print('Found person:')
            print(item)
            action: str = input("""What to do next:
			next - search next record
			menu - return to menu
			: """).strip().lower()
            if action == 'next':
                continue
            elif action == 'menu':
                break
    return None
