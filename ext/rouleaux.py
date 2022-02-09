from random import *

print(random())
print(int(random()*46))
print(int(random()*45)+1)
print(randrange(1,46))
print(randint(1,45))
print(int(random()*45)+1)
print(randrange(1,46))
print(randint(1,45))
num = [5,2,1,3,4]
print(num)
num.sort()
print(num)
num.reverse()
print(num)

for waiting in range(5):
    print('Waiting Number: {0}' .format(waiting))
    
students = [1, 2, 3, 4, 5]
print(students)
students = [ i+100 for i in students]
print(students)
students = ['kim', 'Lee', 'Moon']
print(students)
students = [ len(i) for i in students]
print(students)

def deposit(balance, money):
    print("Deposit done. Your balance is {0}$." .format(balance + money))
    return balance + money

balance = 0
balance = deposit(balance, 1000)
print(balance)

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

commission, balance = withdraw_night(balance, 500)
print(commission)
print(balance)


scores = {'Math':0, 'English':100, 'Lingala':50}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=': ')

for num in range(1,21):
    print('Waiting Number: ' + str(num).zfill(3))

"""score_file = open('score.txt', 'w', encoding = 'utf8')
print('Math: 0', file = score_file)
score_file.close()

score_file = open('score.txt', 'a', encoding = 'utf8')
score_file.write('Science: 80')
score_file.write("\nCoding: 100")
score_file.close()

score_file = open('score.txt', 'r', encoding = 'utf8')
print(score_file.read())
score_file.close()"""
"""
import pickle
profile_file = open('profile.pickle', 'wb')
profile = {'name':'Park', 'age':30, 'job':['commercant', 'trader', 'coding']}
pickle.dump(profile, profile_file)
profile_file.close()

profile_file = open('profile.pickle', 'rb')
profile = pickle.load(profile_file)
print(profile)
profile_file.close()"""



class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} created" .format(name))
    def move(self, location):
        print("{0} is going to {1}. [speed{2}]" .format(self.name, location, self.speed))
    
    def damaged(self, damage):
        print("{0} is damaged {1}." .format(self.name, damage))
        self.hp -= damage
        print("{0} has {1} hp" .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} is destroyed" .format(self.name))
            
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location):
        print("{0} is attacking to {1}. [OP: {2}]" .format(self.name, location, self.damage))
        
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "marine", 40, 1, 5) #name, hp, speed, OP
        
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} using stimpack hp 10 damaged." .format(self.name))
        else:
            print("{0} HP not enough." .format(self.name))

class Tank(AttackUnit):
    sieze_developed = False
    
    def __init__(self):
        AttackUnit.__init__(self, "tank", 150, 1, 35)
        self.seize_mode = False
    
    def set_sieze_mode(self):
        if Tank.seize_developed == False:
            return
        if self.seize_mode == False:
            print("{0} changing to be sieze mode." .format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} changing to be normal mode." .format(self.name))
            self.damage /= 2
            self.seize_mode = False
            
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0} is flying to {1}.[speed {2}]" .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    def move(self, location):
        self.fly(self.name, location)
        
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, 'wraith', 80, 20, 5)
        self.cloaked = False
        
    def cloaking(self):
        if self.cloaked == True:
            print("{0} cloaking mode terminated." .format(self.name))
            self.cloaked = False
        else:
            print("{0} cloaking mode on" .format(self.name))
            self.cloaked = True
