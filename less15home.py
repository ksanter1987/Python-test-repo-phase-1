def with_item(iterable, start = 0):
	n = start
	for item in iterable:
		yield n, item
		n += 1

some_obj = ['1', '2', '3', '4', '5']
print(list(with_item(some_obj)))





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
