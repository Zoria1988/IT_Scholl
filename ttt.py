import math
import datetime

class Equipment():
	"""It is a program of electronic equipment in my kitchen"""

	def __init__(self, name, price, date_of_buying, electriciry_per_day, implementation_period, description=''):
		self.name = name
		self.price = price
		date_param = date_of_buying.split('-')
		year = int(date_param[0])
		month = int(date_param[1])
		day = int(date_param[2])
		self.date_of_buying = datetime.date(year, month, day)
		self.electriciry_per_day = electriciry_per_day
		self.implementation_period = implementation_period
		self.description = description
		print('in __init__ {} {} {} {} {} {}'.format(self.name, self.price, self.date_of_buying, self.electriciry_per_day, self.implementation_period, self.description))

	def __setattr__(self, name, value):
		if name == 'price' and not isinstance(value, int):
			raise TypeError('static types')
		return super().__setattr__(name, value)

	def get_electricity_costs(self, cost=0.9):
		""""How much you should pay for electricity equipment during the month"""
		return round(self.electriciry_per_day * 31 * cost,2)

	def get_used_years(self):
		"""How years you use your equipment"""
		date_now = datetime.date.today()
		years = date_now.year - self.date_of_buying.year
		if date_now.month < self.date_of_buying.month:
			years -= 1
		elif date_now.month == self.date_of_buying.month and date_now.day < self.date_of_buying.day:
			years -= 1
		
		def get_implementation():
			if years > self.implementation_period:
				print('You should change your equipment!')
			else:
				print('You can use your equipment')
		get_implementation()
		return str(years)



oven = Equipment('oven', 100, '1952-01-02', 1, 10, 'it is a black')


print('You must pay', oven.get_electricity_costs())
print('Years of use equipment', oven.get_used_years())

#print(dir(oven))
