''' write codes with codes below to build a managing program.
ex)
there are 3 real estates for sale
Gangnam APT for sale, 10m$ built in 2010
Mapo Office APT for JS, 5m$ built in 2007
Songpa Small APT for monthly rent, 5k$/500$ built in 2000
'''


class House:
	# initialize
	def __init__(self, location, house_type, deal_type, price, completion_year):
		self.location = location
		self.house_type = house_type
		self.deal_type = deal_type
		self.price = price
		self.completion_year = completion_year
		
	def show_detail(self):
		print(self.location, self.house_type,
		"for", self.deal_type,
		",", self.price,
		"built in", self.completion_year) 

house = []		
house1 = House("Gangnam", "APT", "sale", "10m$", "2010")
house2 = House("Mapo", "Office APT", "JS", "5m$", "2007")
house3 = House("Songpa", "Small APT", "monthly rent", "5k$/500$", "2000")

house.append(house1)
house.append(house2)
house.append(house3)

print("there are", len(house), "real estates for sale")
for i in house:
	i.show_detail()
