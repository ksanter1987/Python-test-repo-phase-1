'''
Task 1
Create your own implementation of a built-in function enumerate, named `with_index`, 
which takes two parameters: `iterable` and `start`, default is 0. Tips: see the 
documentation for the enumerate function
'''
def with_item(iterable, start = 0):
	n = start
	for item in iterable:
		yield n, item
		n += 1

some_obj = ['1', '2', '3', '4', '5']
some_list = range(3, 15)
print(list(with_item(some_obj)))
print(list(with_item(some_list)))

'''
Task 2
Create your own implementation of a built-in function range, named in_range(), 
which takes three parameters: `start`, `end`, and optional step. Tips: See the 
documentation for `range` function
'''
def in_range(start, end, step = 1):
	if type(start) == int and type(end) == int and type(step) == int and start < end and step > 0:
		while start < end:
			yield start
			start += step
	elif type(start) == int and type(end) == int and type(step) == int and start > end and step < 0:
		while start > end:
			yield start
			start += step
	else:
		raise ValueError

print(list(in_range(2, 18, 3)))
print(list(in_range(19, -5, -4)))

'''
Task 3
Create your own implementation of an iterable, which could be used inside for-in loop. 
Also, add logic for retrieving elements using square brackets syntax.
'''
class SomeIterable:
	def __init__(self, iterable):
		self.__iter = iterable

	def __iter__(self):
		return iter(self.__iter)

	def __getitem__(self, index):
		return self.__iter[index]

some_constr = SomeIterable({1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g'})
print(some_constr[6])
print()
for item in some_constr:
	print(item)
print()

'''
Task 3_Other
'''
class GameCollection:
	def __init__(self, *args):
		self.game_collection = list(args)

	def __iter__(self):
		return iter(self.game_collection)

	def __getitem__(self, index):
		return self.game_collection[index]

games = GameCollection('Counter Strike', 'Metro', 'WoW', 'CoD', 'Overwatch')
print(f'Today I wonna play {games[4]} !!!')
print()
for i in games:
	print(i)
'''