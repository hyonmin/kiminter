'''class is a kind of machine which can produce a same one repeatly.
Things created through the class are called 'object'.
Objects are instances.
'''

class Unit:
	def  __init__(self, name, hp, speed):
    # __init__ called constructor. Even you do not call it,
    # it is just exacuted automatically.

		self.name = name
		self.hp = hp
		self.speed = speed
		print("A {0} is created. HP: {1}" .format(self.name, self.hp))
	def move(self, location):
		print("Ground unit moves")
		print("{0} is going to the direction {1} with speed {2}." .format(self.name, location, self.speed))

	def damaged(self, damage):
		print("{0} has been attacked. Damage:{1}" .format(self.name, damage))
		self.hp -= damage
		print("{0}'s HP: {1}" .format(self.name, self.hp))
		if self.hp <= 0:
			print("{0} Dead..." .format(self.name))

class Flyable:
	def __init__(self, flying_speed):
		self.flying_speed = flying_speed
		
	def fly(self, name, location):
		print("{0} is flying to the direction {1} with speed {2}." .format(name, location, self.flying_speed))

class AttackUnit(Unit):
	def __init__(self, name, hp, damage, speed):
		Unit.__init__(self, name, hp, speed)
		self.damage = damage

	def attack(self, location):
		print("{0} attacks to {1} direction. Damage: {2}" .format(self.name, location, self.damage))



class FlyableAttackUnit(AttackUnit, Flyable):
	def __init__(self, name, hp, damage, flying_speed):
		AttackUnit.__init__(self, name, hp, damage, 0)
		Flyable.__init__(self, flying_speed)
		
	def move(self, location):
		print("Aero Unit Move")
		self.fly(self.name, location)
		
class BuildingUnit(Unit):
	def __init__(self, name, hp, location):
		Unit.__init__(self, name, hp, 0)
		self.location = location
		
		
firebat1 = AttackUnit("firebat", 50, 16, 2)
firebat1.attack("5'Oclock")
firebat1.move("5'Oclock")
firebat1.damaged(25)
firebat1.damaged(30)
valkyrie1 = FlyableAttackUnit("Valkyrie", 200, 6, 5)
valkyrie1.fly(valkyrie1.name, "11'Oclock")
valkyrie1.move("11'Oclock")
