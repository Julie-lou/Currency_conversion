import unittest
from currency_conversion import currency_conversion


class ClassroomUnitTests(unittest.TestCase):
    def setUp(self):
        # Setup code here (if required, replace the 'pass')
        pass

    def tearDown(self):
        # Teardown code here (if required, replace the 'pass')
        pass

    def test_current_conversion(self):
        self.assertEqual(currency_conversion('USD', 2), 8000)
        self.assertEqual(currency_conversion('usd', 3), 12000)
        self.assertEqual(currency_conversion('Yuan', 3), 1929)
        self.assertEqual(currency_conversion('batH', 2), 246)
        self.assertEqual(currency_conversion('Yen', 2), 'not found')
        self.assertEqual(currency_conversion('yuan', 'ab'), 'invalid amount')


if __name__ == '__main__':
    unittest.main()
