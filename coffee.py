class Coffee:
	def __init__(self, radius, ingredients):
		self.ingredients = ingredients
		self.radius = radius
	def __repr__(self):
		return f'Coffee({self.radius!r},{self.ingredients!r})'
		
	def capacity(self):
		return self.hemisphere(self.radius)
	@classmethod
	def Latte(cls):
		return cls(2,['water', 'bean', 'milk'])
	@classmethod	
	def Mocha(cls):
		return cls(2,['water', 'bean', 'butter', 'chocolate'])
	@classmethod	
	def Cappuccino(cls):
		return cls(2,['water', 'bean', 'milk foam'])
	@classmethod	
	def Irish(cls):
		return cls(2,['water', 'bean', 'butter', 'suger', 'whisky'])
	
	@staticmethod
	def hemisphere(r):
		return 2/3*math.pi*r**3
		
	