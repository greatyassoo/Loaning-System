from django.test import TestCase
from unittest.mock import patch
from .models import Bank


class BankModelTests(TestCase):

    @patch('bank_staff.models.Bank.objects.get')
    @patch('bank_staff.models.Bank.save')
    def test_add_funds(self, mock_save, mock_get):
        # arrange
        mock_bank = Bank(total_funds=1000.00)
        mock_get.return_value = mock_bank

        # act
        Bank.add_funds(500.00)

        # assert
        self.assertEqual(mock_bank.total_funds, 1500.00)
        mock_save.assert_called_once()

    @patch('bank_staff.models.Bank.objects.get')
    @patch('bank_staff.models.Bank.save')
    def test_remove_funds(self, mock_save, mock_get):
        # arrange
        mock_bank = Bank(total_funds=1000.00)
        mock_get.return_value = mock_bank

        # act
        Bank.remove_funds(300.00)

        # assert
        self.assertEqual(mock_bank.total_funds, 700.00)
        mock_save.assert_called_once()
