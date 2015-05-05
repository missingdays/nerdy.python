class Set():
	values = []	

	def __init__(self, element=None):
		if type(element) is list: 
			for elem in element:
				if not elem in self.values:
					self.values.append(elem)
		elif element is not None:
			if not element in self.values:
				self.values.append(element)

	def set_elem(self, element):
		if not element in self.values:
			self.values.append(element)

	def set_array(self, array):
		for elem in array:
			if not elem in self.values:
				self.values.append(elem)
	def get_values(self):
		return self.values
	
	def elem_exists(self, element):
		return element in self.values 	
my_set = Set()
my_set.set_elem(5)
my_set.set_array([5,4,3])
print(my_set.get_values())
