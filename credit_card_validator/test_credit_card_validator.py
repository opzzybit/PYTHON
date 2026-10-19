from unittest import TestCase

from Credit_Card_Validator import  credit_card_type_confirmation

class TestCreditCardValidator(TestCase):

    def test_the_credit_card_type(self):
        credit_number = credit_card_type_confirmation("4384324354563435")
        expected_type = " Visa Card"
        
        self.assertEqual(credit_number,expected_type)
