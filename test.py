# Наш перший коментар
int_value = 1 # ціле число, integer or int
negative_int_value = -1 # ціле відємне число, integer or int, negative
print (int_value)
print (negative_int_value)

print()

float_value = 1.234 #  float, дробове число, число з плаваючою точкою
print (float_value)

print()

string_value = 'Text 1' # string or str, стрічка with quotes
print(string_value)

print()

string_second = "Text 2" # string or str, стрічка with double quotes
print (string_second)

print()

meaningful_sentence = "Once upon a time ..... don't"

meaningful_sentence_two = 'Once upon a time ..... don\'t   \\m/'   # екранування спецсимволів
print (meaningful_sentence_two)

print()

meaningful_sentence_three = 'The first line \n\tThe Second one'    # \n переніс стрічки на новий рядок, \t табуляція
print (meaningful_sentence_three)

print()

very_long_string = 'Very long long long sentence without any sence or context but stil this one is very long and hardly readable'   # 80символів рекомендована довжина
print (very_long_string)

print()

very_long_string_2 = 'Very long long long sentence without any sence or context' +\
'but stil this one is very long and hardly readable'   # 80символів рекомендована довжина  
print (very_long_string_2)

print()

paragraph_text_1 = """First line
second line
third line
...
last line"""
print (paragraph_text_1)

print()

paragraph_text_2 = '''First line
second line
third line
...
last line'''
print (paragraph_text_2)

negative_statement = False  # негативне твердження, False actually is 0
positive_statement = True # позитивне твердження, True is actually is 1

print (negative_statement)

print ()

print (positive_statement)


#Calculations
x = 1
y = 2
print (x + y)
print (x - y)
print (x / y)
print (x * y)
print (x % y) # mod 2
print (x // y)

print (f'Sum: {x} + {y} = {x + y}')
print (f'Ext: {x} - {y} = {x - y}')
print (f'Div: {x} / {y} = {x / y}')
print (f'Mult: {x} * {y} = {x * y}')
print (f'Modulo: {x} mod {y} = {x % y}')


print (f'{paragraph_text_2}')


x = 3
y = 3
comparison_result = x == y
print (f'Comparing {x} and {y}: {comparison_result}')

print (f'Is {x} more than {y}: {x > y}')

print (f'Is {x} less than {y}: {x < y}')

print (f'Is {x} more or equal than {y}: {x >= y}')

print (f'Is {x} less or equal than {y}: {x <= y}')


