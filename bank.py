class Account():
	def __init__(self, name):
		self.name = name
		self.balance = 0.0
	def apply_interest(self, interest):
		self.balance *= interest