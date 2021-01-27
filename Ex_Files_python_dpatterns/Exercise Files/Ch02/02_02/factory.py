class Dog:

	"""A simple dog class"""

	def __init__(self, name):
		self._name = name

	def speak(self):
		return ("My name is {0} and I do Woof:".format(self._name))

class Cat:

	"""A simple cat class"""

	def __init__(self, name):
		self._name = name

	def speak(self):
		return ("My name is {0} and I do Meow:".format(self._name))

def get_pet(pet):
	"""The Factory method"""

	pets = dict(dog = Dog("Hope"), cat = Cat("Peace"))

	return pets[pet]

d = get_pet("dog")
print(d.speak())

d = get_pet("cat")
print(d.speak())