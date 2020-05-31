'''
Task 1
School
Make a class structure in python representing people at school. Make a base class called Person,
a class called Student, and another one called Teacher. Try to find as many methods and attributes
as you can which belong to different classes, and keep in mind which are common and which are not.
For example, the name should be a Person attribute, while salary should only be available to the teacher.
'''
class Person:
	def __init__(self, name, gender, age):
		self.name = name
		self.gender = gender
		self.age = age
class Student(Person):
	def __init__(self, name, gender, age, grade, course):
		super().__init__(name, gender, age, *args, **kwargs) #super() Person
		self.grade = grade
		self.course = course
class Teacher(Person):
	def __init__(self, name, gender, age, salary, seniority):
		super().__init__(name, gender, age)
		self.salary = salary
		self.seniority = seniority


'''
Task 2
Mathematician
Implement a class Mathematician which is a helper class for doing math operations on lists
The class doesn't take any attributes and only has methods:
square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
'''
class Mathematician:
	def square_nums(self, some_list):
		square_nums = [x**2 for x in some_list]
		print(square_nums)
	def remove_positives(self, some_list):
		remove_positives = [x for x in some_list if x < 0]
		print(remove_positives)
	def filter_leaps(self, some_list):
		filter_leaps = [x for x in some_list if x % 4 == 0]
		print(filter_leaps)
m = Mathematician()
m.square_nums([1, 3, 4, 7])
m.remove_positives([26, -11, -8, 13, -90])
m.filter_leaps([2001, 1884, 1995, 2003, 2020])



'''
Task 3
Product Store
Write a class Product that has three attributes:
-type
-name
-price
Then create a class ProductStore, which will have some Products and will operate with all
products in the store. All methods, in case they can’t perform its action, should raise ValueError
with appropriate error information.
Tips: Use aggregation/composition concepts while implementing the ProductStore class.
You can also implement additional classes to operate on a certain type of product, etc.
Also, the ProductStore class must have the following methods:

-add(product, amount) - adds a specified quantity of a single product with a predefined price premium
for your store(30 percent)

-set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified
by input identifiers (type or name). The discount must be specified in percentage

-sell_product(product_name, amount) - removes a particular amount of products from the store if available,
in other case raises an error. It also increments income if the sell_product method succeeds.

-get_income() - returns amount of many earned by ProductStore instance.

-get_all_products() - returns information about all available products in the store.

-get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
'''
class Product:
	product_type = ''
	name = ''
	price = 0


	def __init__(self, product_type, name, price):
		try:
			if isinstance(product_type, str) is True and isinstance(name, str) and (isinstance(price, int) or isinstance(price, float)):
				self.product_type = product_type
				self.name = name
				self.price = price
			else:
				raise ValueError('Wrong data type')
		except ValueError as e:
			print(e)


	def __str__(self):
		return f'{self.name} = {self.price} $'


	def __repr__(self):
		return f'{self.name} = {self.price} $'


class ProductStore:
	amount = 0
	profit = 0
	storage = []


	def add(self, product, amount):
		result = {}
		result['product'] = product
		result['amount'] = amount
		product.price *= 1.3
		self.storage.append(result)


	def set_discount(self, identifier, percent,):
		try:
			if isinstance(percent, int) is True:
				for item in self.storage:
					store_product = item['product']
					if store_product.product_type == identifier or store_product.name == identifier:
						store_product.price = store_product.price * (100 - percent) / 100
			else:
				raise ValueError('Wrong percentage input')
		except ValueError as e:
			print(e)


	def sell_product(self, product_name, amount):
		try:
			if isinstance(amount, int):
				for item in self.storage:
					store_product = item['product']
					if store_product.name == product_name and amount <= item['amount']:
						item['amount'] -= amount
						self.profit = amount * store_product.price
					elif store_product.name == product_name and amount > item['amount']:
						raise ValueError('We do not have so many products')
			else:
				raise ValueError('Enter integer amount')
		except ValueError as e:
			print(e)


	def get_income(self):
		return print(f'Our profit is {self.profit} $')


	def get_all_products(self):
		return print(self.storage)


	def get_product_info(self, product_name):
		for item in self.storage:
			store_product = item['product']
			if store_product.name == product_name:
				product_info = store_product.name, item['amount']
				return print(f'{product_info}')



product1 = Product('Sport', 'Football T-Shirt', 100)
product2 = Product('Sport', 'Football boots', 50)
product3 = Product('Fruit', 'Apple', 10)
store = ProductStore()
store.add(product1, 10)
store.add(product2, 15)
store.add(product3, 100)
print(store.storage)
print()
store.set_discount('Apple', 10)
print(store.storage)
print()
store.sell_product('Apple', 10)
print(store.storage)
print()
store.get_income()
print()
store.get_all_products()
print()
store.get_product_info('Apple')


'''
Task 4
Custom exception

Create your custom exception named `CustomException`, you can inherit from base Exception class, but extend its 
functionality to log every error message to a file named `logs.txt`. Tips: Use __init__ method to extend functionality for saving messages to file
'''
class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
    	return f'Error with message: {self.msg}'
    def __repr__(self):
    	return f'Error with message: {self.msg}'
a = input("Input positive integer: ")
try:
	a = int(a)
	if a < 0:
		raise CustomException('You give negative!')
except CustomException as e:
	with open('logs.txt', 'a') as log_file:
		log_file.write(str(e) + '\n')
	print(e)
else:
	print(a)
