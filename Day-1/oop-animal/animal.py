class Animal(object):
	"""The Animal class"""

	def __init__(self):
		self.feed = True
		self.multicellular = True

	def movement(self, moves_by):
		if type(moves_by) == str:
			self.moves_by = moves_by
		return "The animal moves by: %s" % (self.moves_by)

class Bird(Animal):
	"""The Bird class"""

	def skin_covered_with(self):
		self.cover = "feathers"
		return "The animal is covered with: %s" % (self.cover)

	def how_it_moves(self):
		self.moves_by = "flying"
		return super(Bird,self).movement(self.moves_by)

class Mammal(Animal):
	"""The Mammal class"""

	def skin_covered_with(self, cover="Fur"):
		if type(cover) == str:
			self.cover = cover
		return "The animal is covered with: %s" % (self.cover)

	def how_it_moves(self):
		self.moves_by = "walking"
		return super(Bird,self).movement(self.moves_by)
