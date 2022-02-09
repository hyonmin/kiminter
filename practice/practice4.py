# function

def open_account():
	print("New account created")
	
def deposit(balance, money):
	print("Deposit done. Your balance is {0} $." .format(balance + money))
	return balance + money
	
def withdraw(balance, money):
	if balance >== money:
		print("Withdraw done. Your balance is {0} $." .format(balance - money))
		return balance - money
	else:
		print("Withdraw denied. Your balance is {0} $." .format(balance))
		return balance
		
def withdraw_night(balance, money):
	commission = 1
	return commission, balance - money - commission
balance = 0
balance = diposit(balance, 1000)
balance = withdraw(balance, 2000)
balance = withdraw(balacne, 500)
print(balance)

commission, balance = withdraw_night(balance, 500)  # tuple

print("commission: {0}, your balance is {1} $." .format(commissioin, balance)) 

