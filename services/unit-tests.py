import unittest
import currencyConversion


class TestCurrencyConversion(unittest.TestCase):

    def testConversion(self):
        currencyConversion.requestXML()
        self.assertGreater(currencyConversion.convertCurrency("USD", 100, "EUR"), 0)


unittest.main()
