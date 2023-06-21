#Maggie Mulhall
#Unit Tests of Bank Application

#Initializations
import unittest
from pydoc import *
from Bank import BankManager,Account,Bank,BankUtility,CoinCollector

#Initialize objects
manager=BankManager()
bank=Bank()

class TestAccount(unittest.TestCase):

    #Account Class Tests
    #Methods Tested: isValidPIN, deposit, withdraw
    def test_Account(self):
        account=Account("Maggie","Mulhall","000001234","5678","19","09876543")
        self.assertEqual(Account.isValidPIN(account,"1234"),False)
        self.assertEqual(Account.isValidPIN(account,"5678"),True)
        self.assertEqual(Account.deposit(account,5),24)
        self.assertIsNot(Account.deposit(account,5),25)     
        self.assertEqual(Account.withdraw(account,6),23)  
        self.assertIsNot(Account.withdraw(account,1),24)            

    #BankUtility Class Tests
    #Methods Tested: generateRandomInteger, isNumeric, ConvertFromDollarsToCents
    def test_BankUtility(self):
        self.assertEqual(BankUtility.isNumeric("6"),True)
        self.assertEqual(BankUtility.isNumeric("hello"),False)
        self.assertEqual(BankUtility.convertFromDollarsToCents(3.79),379)
        self.assertIsNot(BankUtility.convertFromDollarsToCents(9.00),90)
        Random=BankUtility.generateRandomInteger(1000,9999)
        self.assertLessEqual(Random,9999)
        self.assertGreaterEqual(Random,1000)
    
    #Coincollector Class Tests
    #Method Tested: parseChange
    def test_Coincollector(self):
        collector=CoinCollector()
        self.assertEqual(CoinCollector.parseChange(collector,"PPQHND"),92)
        self.assertIsNot(CoinCollector.parseChange(collector,"WHDMP"),156)
        self.assertIsNot(CoinCollector.parseChange(collector,"PPNNDDQQHHWW"),382)     

    #Bank Class Tests
    #Methods Tested: AddAccountToBank, removeAccountFromBank
    def test_Bank(self):
        self.bank=Bank()
        self.accounts = [None] * 100
        self.assertEqual(Bank.addAccountToBank(bank,"00000001"),True)
        self.assertEqual(Bank.addAccountToBank(bank,"00000099"),True)
        Bank.addAccountToBank(bank,"00000002")
        Bank.addAccountToBank(bank,"00000003")
        self.assertEqual(Bank.removeAccountFromBank(bank,"00000003"),True)
        self.assertEqual(Bank.removeAccountFromBank(bank,"00000003"),False)
        
#Call Unit tests
if __name__ == '__main__':
    unittest.main()