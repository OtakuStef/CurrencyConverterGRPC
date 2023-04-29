import unittest
import currencyConversion


class TestCurrencyConversion(unittest.TestCase):

    def testConversion(self):
        currencyConversion.requestXML()
        self.assertGreater(currencyConversion.convertCurrency("USD", 100, "EUR"), 0)
        self.assertGreater(currencyConversion.convertCurrency("USD", 100, "JPY"), 0)
        self.assertEqual(currencyConversion.convertCurrency("USD", 0, "EUR"), 0)


unittest.main()
