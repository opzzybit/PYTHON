import unittest

from Credit_Card_Validator import *

class TestCreditCard(unittest.TestCase):


    def test_visa_card(self):
        numbers = [4, 5, 3, 9, 1, 4, 8, 8,
                   5, 0, 3, 4, 3, 6, 4, 6]

        result = get_credit_card_type(numbers)
        self.assertEqual(result, " Visa Card")

    def test_mastercard(self):
        numbers = [5, 5, 5, 5, 5, 5, 5, 5,
                   5, 5, 5, 5, 5, 5, 5, 5]

        result = get_credit_card_type(numbers)

        self.assertEqual(result, "Master Card")

    def test_discover_card_(self):
        numbers = [6, 0, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1]

        result = get_credit_card_type(numbers)

        self.assertEqual(result, "Discover card")


    def test_credit_card_length(self):
        numbers = [4, 5, 3, 9, 1, 4, 8, 8,
                   5, 0, 3, 4, 3, 6, 4, 6]

        result = get_credit_card_length(numbers)

        self.assertEqual(result, 16)

    
    def test_valid_card_length(self):
        numbers = [4, 5, 3, 9, 1, 4, 8, 8,
                   5, 0, 3, 4, 3, 6, 4, 6]

        result = get_confirmation_of_credit_card_length(numbers)

        self.assertEqual(result, "Valid card length")

    def test_invalid_card_length(self):
        numbers = [4, 5, 3, 9, 1, 4, 8, 8, 5, 0]

        result = get_confirmation_of_credit_card_length(numbers)

        self.assertEqual(
            result,
            "Error Message: you exceeded the card limit (13 or 16 length)"
        )

    
    def test_sum_of_second_digit_calculation(self):
        numbers = [4, 5, 3, 9, 1, 4, 8, 8,
                   5, 0, 3, 4, 3, 6, 4, 6]

        result = sum_of_card_second_digit_from_right_to_left(numbers)

        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)

    
    def test_sum_of_odd_numbers(self):
        numbers = [4, 5, 3, 9, 1, 4, 8, 8,
                   5, 0, 3, 4, 3, 6, 4, 6]

        result = sum_of_credit_card_odd_numbers(numbers)

        self.assertEqual(result, 35)

   
    def test_sum_of_credit_card_validations(self):
        result = sum_of_credit_card_validations(20, 15)

        self.assertEqual(result, 35)

    
    def test_valid_credit_card(self):
        result = final_credit_card_confirmation(30)

        self.assertEqual(result, "VALID ")

    def test_invalid_credit_card(self):
        result = final_credit_card_confirmation(31)

        self.assertEqual(result, "INVALID")



