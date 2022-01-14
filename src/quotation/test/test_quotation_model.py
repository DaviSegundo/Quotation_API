"""Module to test Quotation model
"""

import requests
from django.test import TestCase
from quotation.models import Quotation
from jsonschema import validate

class QuotationModelTestCase(TestCase):
    """Class to test data of quotation.
    """
    def setUp(self):
        self.quotation_valid = Quotation(
            date='2022-01-12',
            response_date={
                "date": "2022-01-12",
                "base": "USD",
                "rates": {
                    "EUR": 0.8795074758135444,
                    "USD": 1.0,
                    "JPY": 115.3825857519789,
                    "BGN": 1.7201407211961302,
                    "CZK": 21.480211081794195,
                    "DKK": 6.544766930518909,
                    "GBP": 0.7329639401934916,
                    "HUF": 313.08707124010556,
                    "PLN": 3.989357959542656,
                    "RON": 4.349428320140721,
                    "SEK": 9.027264731750218,
                    "CHF": 0.9222515391380827,
                    "ISK": 129.28759894459102,
                    "NOK": 8.730870712401055,
                    "HRK": 6.617414248021108,
                    "RUB": 74.54344766930518,
                    "TRY": 13.713456464379947,
                    "AUD": 1.3862796833773088,
                    "BRL": 5.58117854001759,
                    "CAD": 1.2542656112576955,
                    "CNY": 6.365787159190853,
                    "HKD": 7.795074758135444,
                    "IDR": 14332.392260334213,
                    "ILS": 3.1139841688654353,
                    "INR": 73.90369393139841,
                    "KRW": 1190.2110817941953,
                    "MXN": 20.39155672823219,
                    "MYR": 4.186015831134565,
                    "NZD": 1.4753737906772206,
                    "PHP": 51.08179419525066,
                    "SGD": 1.3507475813544416,
                    "THB": 33.36499560246262,
                    "ZAR": 15.448109058926999
                }}
        )

    def test_quotation_create(self):
        """Testing if a creation is correct
        """
        self.assertEqual(self.quotation_valid.date, '2022-01-12')
        self.assertEqual(self.quotation_valid.response_date, {
                "date": "2022-01-12",
                "base": "USD",
                "rates": {
                    "EUR": 0.8795074758135444,
                    "USD": 1.0,
                    "JPY": 115.3825857519789,
                    "BGN": 1.7201407211961302,
                    "CZK": 21.480211081794195,
                    "DKK": 6.544766930518909,
                    "GBP": 0.7329639401934916,
                    "HUF": 313.08707124010556,
                    "PLN": 3.989357959542656,
                    "RON": 4.349428320140721,
                    "SEK": 9.027264731750218,
                    "CHF": 0.9222515391380827,
                    "ISK": 129.28759894459102,
                    "NOK": 8.730870712401055,
                    "HRK": 6.617414248021108,
                    "RUB": 74.54344766930518,
                    "TRY": 13.713456464379947,
                    "AUD": 1.3862796833773088,
                    "BRL": 5.58117854001759,
                    "CAD": 1.2542656112576955,
                    "CNY": 6.365787159190853,
                    "HKD": 7.795074758135444,
                    "IDR": 14332.392260334213,
                    "ILS": 3.1139841688654353,
                    "INR": 73.90369393139841,
                    "KRW": 1190.2110817941953,
                    "MXN": 20.39155672823219,
                    "MYR": 4.186015831134565,
                    "NZD": 1.4753737906772206,
                    "PHP": 51.08179419525066,
                    "SGD": 1.3507475813544416,
                    "THB": 33.36499560246262,
                    "ZAR": 15.448109058926999
                }})

    def test_quotation_show_all(self):
        """Testing show_all function
        """
        data = self.quotation_valid.show_all()
        response = requests.get('https://api.vatcomply.com/rates?base=USD').json()
        self.assertEqual(data, response)
        self.assertEqual(type(data), type(response))

    def test_quotation_get_date(self):
        """Testing method get date of a response
        """
        date = self.quotation_valid.get_date(self.quotation_valid.response_date)
        self.assertEqual(date, '2022-01-12')
        self.assertEqual(type(date), str)

    def test_quotation_get_quotation_currency(self):
        """Testing if method return currency correct
        """
        currency = self.quotation_valid.get_quotation_currency("brl")
        currencys = []
        currencys_check = []
        for k in dict(self.quotation_valid.response_date).get("rates"):
            currencys.append(k)
        for j in requests.get('https://api.vatcomply.com/rates?base=USD').json().get("rates"):
            currencys_check.append(j)
        self.assertEqual(type(currency), dict)
        self.assertEqual(currencys, currencys_check)

    def test_schema_validation(self):
        """Testing struct of the schema
        """
        schema = {
            "type" : "object",
            "properties" :{
            "date" : {"type" : "string"},
            "response_date" : {"type" : "object"}
            }
        }

        validate(self.quotation_valid.response_date, schema=schema)
