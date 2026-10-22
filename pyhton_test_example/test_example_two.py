import unittest 

from example_two import * 

class TestExampleTwo (unittest.Testcase):

    def test_that_a_newAccount_HasAZeroBalance(self):
    
        account_balance = 0.0
        
        self.assertEqual(check_balance(), account_balance)
        

