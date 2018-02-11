import unittest
from bank import Bank, Account, SavingAccount, CurrentAccount
import time
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        self.bank = Bank(interest_interval=1)
 
    def test_bank_current_interest(self):
        self.bank.create_account("Tasnia", "current account", 1.0)
        time.sleep(2)
        self.bank.apply_interest()
        self.assertEqual("£" + str(self.bank.accounts[0].balance), "£" + str(1.0))

 
    def test_bank_saving_interest(self):
        self.bank.create_account("Noel", "saving account", 1.0)
        time.sleep(2)
        self.bank.apply_interest()
        self.assertEqual("£" + str(self.bank.accounts[0].balance), "£" + str(1.5**2))

 
if __name__ == '__main__':
    unittest.main()