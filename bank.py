# -*- coding: utf-8 -*- 
from datetime import datetime, timedelta
import time

#classes used as blueprints
#external "main" code runs class Bank, class Bank runs class Account.
class Account():
	def __init__(self, name):
		#self. allows you to attach variables to the account being created
		self.name = name
		self.balance = 0.0
		self.account_created = datetime.now()
		#time stamp for each account created
		self.interest = 1.1

	def apply_interest(self):
		self.balance *= self.interest


class SavingAccount(Account):
	def __init__(self, name):
		super().__init__(name)
		self.interest = 1.5

class CurrentAccount(Account):
	def __init__(self, name):
		super().__init__(name)
		self.interest = 1.0

class Bank():
	def __init__(self):
		#accounts created in Account stored as list in Bank
		self.accounts = []
		#set interval at which interest is applied to per minute
		self.interest_interval = timedelta(minutes=1)
	

	def create_account(self, name, account_type):
		account = Account(name)
		self.accounts.append(account)

	def apply_interest(self):
		#conditions to apply interest: loop through accounts list in Bank, time now is greater than time past
		#check against set interval
		for account in self.accounts:
			if datetime.now() - account.account_created > self.interest_interval:
				account.apply_interest()
		

if __name__ == "__main__":
	#import pdb
	#pdb.set_trace()
	"""bank = Bank()
	bank.create_account("Tasnia")
	bank.accounts[0].balance = 1.0
	time.sleep(60)
	bank.apply_interest()
	print "£" + str(bank.accounts[0].balance)"""

	from random import randint

	class_list = [Account, SavingAccount, CurrentAccount]

	for x in range(5):
		bank = Bank()
