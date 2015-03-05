"""Working with Python CLasses!"""
#Social Networking Yo!
import copy

class Person(object):
	"""Information about a person"""
	def __init__(self, firstName, lastName, job ):
		self.firstName = firstName
		self.lastName = lastName
		self.job = job
		self.friends = []

	def __str__(self):
		"""print out details about given person"""
		template = "{f} {l} is a {j}"
		print template.format(f = self.firstName, l = self.lastName, j = self.job)

	def addFriend(self, friend):
		self.friends.append(friend)

	"""def printPerson(self):
		"prints details about specific person
			template = "{f} {l} is a {j}"
			print template.format(f = self.firstName, l = self.lastName, j = self.job)"""
		

keez = Person('Keenan', 'Zucker', 'saint')
scott = Person('Scott', 'Mackinlay', 'bro')
print keez
"""
keez.firstName = 'Keenan'
keez.lastName = 'Zucker'
keez.job  = 'saint'
keez.weight = 190

printPerson(keez)

scott = copy.copy(keez)
scott.job = 'idiot'
scott.firstName = 'Scott'"""

keez.addFriend(scott)

