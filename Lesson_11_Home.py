'''Task 1
School
Make a class structure in python representing people at school. Make a base class called Person,
a class called Student, and another one called Teacher. Try to find as many methods and attributes
as you can which belong to different classes, and keep in mind which are common and which are not.
For example, the name should be a Person attribute, while salary should only be available to the teacher.'''
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

'''
Task 2
Mathematician
Implement a class Mathematician which is a helper class for doing math operations on lists
The class doesn't take any attributes and only has methods:
square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'

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

-get_product_info(product_name) - returns a tuple with product name and amount of items in the store.'''
'''
class Product:
	product_type = ''
	name = ''
	price = 0


	def __init__(self, product_type, name, price):
		self.product_type = product_type
		self.name = name
		self.price = price


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


	def set_discount(self, identifier, percent, identifier_type):
		pass


	def sell_product(self, name, amount):
		for item in self.storage:
			if item == product.name:
				product_name[self.amount] = self.product_name[self.amount - amount]

'''

'''	def set_discount(identifier, percent, identifier_type=’name’):
	def sell_product(product_name, amount):
	def get_income():
	def get_all_products():
	def get_product_info(product_name):
    pass
class ProductStore(Product):
pass
p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product(Food, 'Ramen, 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell(‘Ramen’, 10)
assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)

white_check_markeyesraised_hands
'''
'''
p1 = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Sport', 'Football boots', 50)
s = ProductStore()
s.add(p1, 10)
s.add(p2, 15)
s.sell_product('Football T-Shirt', 4)
print(s.storage)'''









'''Task 4
Custom exception

Create your custom exception named `CustomException`, you can inherit from base 
Exception class, but extend its functionality to log every error message to a file 
named `logs.txt`. Tips: Use __init__ method to extend functionality for saving messages to file'''


log_file = open('logs.txt', 'w')
log_file.close()


class CustomException(Exception):
	def __init__(self, msg):
		self.msg = msg

