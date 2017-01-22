class Account():
	def __init__(self, name):
		self.name = name
		self.balance = 0.0

	def apply_interest(self, interest):
		self.balance *= interest

class Bank():
	def __init__(self):
		self.accounts = []

	def create_account(self, name):
		account = Account(name)
		self.accounts.append(account)

if __name__ == "__main__":
	import pdb
	pdb.set_trace()
	bank = Bank()
	bank.create_account("Tasnia")