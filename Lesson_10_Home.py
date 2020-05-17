'''Task 1
A Person class

Make a class called Person. Make the __init__() method take firstname, lastname, and age as 
parameters and add them as attributes. Make another method called talk() which makes prints 
a greeting from the person containing, for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.'''

'''class Person:
		def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		

	def talk(self):
		print('Hello, my name is', self.first_name, self.last_name, "and I’m", self.age, 'years old')


person1 = Person('Alex', 'Kuvychko', '33')
person1.talk()'''


'''Task 2
Doggy age

Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values 
for a dog’s age. Then create a method `human_age` which returns the dog’s age in human equivalent.'''

class Dog:
	age_factor = 7


	def __init__(self, dogs_age):
		self.dogs_age = dogs_age


	def human_age(self):
		return self.dogs_age * 7


human_eqiv = Dog(6)
print(human_eqiv.human_age())


