# -*- coding: utf-8 -*- 
from datetime import datetime, timedelta
import time
from random import randint

#classes used as blueprints
#external "main" code runs class Bank, class Bank runs class Account.
class Account():
	def __init__(self, name, balance=0.0):
		#self. allows you to attach variables to the account being created
		self.name = name
		self.balance = balance
		self.account_created = datetime.now()
		#time stamp for each account created
		self.interest = 1.1

	def apply_interest(self):
		self.balance *= self.interest

	def __repr__(self):
		return "Name: %s, Account: %s Balance = %s" % (self.name, self.__class__.__name__, self.balance)


class SavingAccount(Account):
	def __init__(self, name, balance=0.0):
		super().__init__(name, balance)
		self.interest = 1.5

class CurrentAccount(Account):
	def __init__(self, name, balance=0.0):
		super().__init__(name, balance)
		self.interest = 1.0

class Bank():
	def __init__(self):
		#accounts created in Account stored as list in Bank
		self.accounts = []
		#set interval at which interest is applied to per second
		self.interest_interval = timedelta(seconds=5)
	

	def create_account(self, name, account_type, account_balance):
		account_types = {"account": Account, "saving account": SavingAccount, "current account": CurrentAccount}
		account_class = account_types[account_type]
		account = account_class(name, balance=account_balance)
		self.accounts.append(account)

	def apply_interest(self):
		#conditions to apply interest: loop through accounts list in Bank, time now is greater than time past
		#check against set interval
		for account in self.accounts:
			if datetime.now() - account.account_created > self.interest_interval:
				account.apply_interest()

def create_random_accounts(bank):

		input_list = ["account", "saving account", "current account"]
		name_list = ["Tasnia", "Noel", "Soeng-ha", "Jintana", "Eddie", "Nat"]

		for x in range(6):
			bank.create_account(name_list[x], input_list[randint(0,2)], float(randint(0,10)))
		

if __name__ == "__main__":
	import pdb
	pdb.set_trace()
	"""bank = Bank()
	bank.create_account("Tasnia")
	bank.accounts[0].balance = 1.0
	time.sleep(60)
	bank.apply_interest()
	print "£" + str(bank.accounts[0].balance)"""

	bank = Bank()

	create_random_accounts(bank)

	for x in bank.accounts:
		print(x)

	time.sleep(6)
	bank.apply_interest()

	for x in bank.accounts:
		print(x)


