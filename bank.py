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

	def apply_interest(self, interest):
		self.balance *= interest


class Bank():
	def __init__(self):
		#accounts created in Account stored as list in Bank
		self.accounts = []
		self.interest = 1.1
		#set interval at which interest is applied to per minute
		self.interest_interval = timedelta(minutes=1)
	

	def create_account(self, name):
		account = Account(name)
		self.accounts.append(account)

	def apply_interest(self):
		#conditions to apply interest: loop through accounts list in Bank, time now is greater than time past
		#check against set interval
		for account in self.accounts:
			if datetime.now() - account.account_created > self.interest_interval:
				account.apply_interest(self.interest)
		

if __name__ == "__main__":
	#import pdb
	#pdb.set_trace()
	bank = Bank()
	bank.create_account("Tasnia")
	bank.accounts[0].balance = 1.0
	time.sleep(60)
	bank.apply_interest()
	print "£" + str(bank.accounts[0].balance)