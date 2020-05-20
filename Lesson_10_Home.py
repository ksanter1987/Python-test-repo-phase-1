'''Task 1
A Person class

Make a class called Person. Make the __init__() method take firstname, lastname, and age as 
parameters and add them as attributes. Make another method called talk() which makes prints 
a greeting from the person containing, for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.'''

class Person:
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		

	def talk(self):
		print('Hello, my name is', self.first_name, self.last_name, "and I’m", self.age, 'years old')


person1 = Person('Alex', 'Kuvychko', '33')
person1.talk()


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


'''Task 3
TV controller
Create a simple prototype of a TV controller in Python. It’ll use the following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' 
exists in the list, or "No" - in the other case.
The default channel turned on before all commands is №1.
Your task is to create the TVController class and methods described above.'''

CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self, channels):
        self.__channels = channels
        self.__current_channel = 0
    

    def turn_channel(self, channel_number):
        self.__current_channel = channel_number - 1
        return self.current_channel()


    def current_channel(self):
        return self.__channels[self.__current_channel]        


    def first_channel(self):
        return self.turn_channel(1)

    
    def last_channel(self):
        return self.turn_channel(len(self.__channels))


    def next_channel(self):
        self.__current_channel = self.__current_channel + 1
        if self.__current_channel < len(self.__channels):
            return self.current_channel()
        else:
            return first_channel()


    def previous_channel(self):
        self.__current_channel = self.__current_channel - 1
        if self.__current_channel > 0:
            return self.current_channel()
        else:
            return self.turn_channel(len(self.__channels))


    def is_exist(self, channel):
        if channel in self.__channels:
            return 'Yes'
        elif channel not in self.__channels:
            return 'No'
        elif isinstance(channel, int) and channel > 0 and channel < len(self.__channels):
            return 'Yes'
        else:
            return 'No'


controller = TVController(CHANNELS)
print(controller.first_channel()) 
print(controller.last_channel()) 
print(controller.turn_channel(1))
print(controller.next_channel()) 
print(controller.previous_channel()) 
print(controller.current_channel()) 
print(controller.is_exist(4)) 
print(controller.is_exist("BBC"))
