# -*- coding: utf-8 -*- 
from datetime import datetime, timedelta
import time


class Account():
	def __init__(self, name):
		self.name = name
		self.balance = 0.0
		self.account_created = datetime.now()

	def apply_interest(self, interest):
		self.balance *= interest


class Bank():
	def __init__(self):
		self.accounts = []
		self.interest = 1.1
		self.interest_interval = timedelta(minutes=1)

	def create_account(self, name):
		account = Account(name)
		self.accounts.append(account)

	def apply_interest(self):
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