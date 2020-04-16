# Lesson 1 Task 2
# Create a python program named “task2”, and use the built-in function `print` in 
# it several times. Try to pass “sep”, “end” params and pass several parameters separated by commas. 
# Also, provide a comment text above each print statement, mentioned above, 
# with the expected output after execution of the particular print statement.

print() # вывод пустой строки
print('Lesson_1') # Вывод строки Lesson_1
print()
print('a','b','c','d','e', sep= '+') # вывод строк 'a', 'b', 'c', 'd', 'e' с строчным разделителем '+'
print()
print('Lesson_1-1', end= ' ') # вывод строки 'Lesson_1-1' с совмещением ее со следующей строкой через ' ' (пробел)
print('Lesson_1-2')
print()
print('Lesson_1-1', end= ' + ') # вывод строки 'Lesson_1-1' с совмещением ее со следующей строкой через ' + ' (пробел, плюс, пробел)
print('Lesson_1-2')
print()
print('Lesson_1-1', end= '\n') # вывод строки 'Lesson_1-1' вывод строки закончивается переносом на новую строку
print('Lesson_1-2')
print()
print(1, 2, 3, 4, 5, 6, 7, sep='\t<', end= '\n\t' ) # Вывод значений 1, 2, 3, 4, 5, 6, 7 с разделителем табуляции и знаком '<' после чего осуществлен перенос на следующую строку плюс табуляция
print('Task is over')
print()
print()


# Lesson 1 Task 3
# Write a program, which has two print statements to print the following text 
# (capital letters “O” and “H”, made from “#” symbols):

#########
#       #
#       #
#       #
#########

#       #
#       #
######### 
#       # 
#       #

# Pay attention that usage of spaces is forbidden, as well as creating the whole 
# result text string using “”” ”””, use ‘\n’ and ‘\t’ symbols instead.

a = '#'
print(a * 9)
print(a,a, sep = 2 * '\t')
print(a,a, sep = 2 * '\t')
print(a,a, sep = 2 * '\t')
print(a * 9, '\n')
print(a,a, sep = 2 * '\t')
print(a,a, sep = 2 * '\t')
print(a * 9)
print(a,a, sep = 2 * '\t')
print(a,a, sep = 2 * '\t')