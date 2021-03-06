"""Module to test Quotation Serializer
"""

from django.test import TestCase
from quotation.models import Quotation
from quotation.serializer import QuotationSerializer

class QuotationSerializerTestCase(TestCase):
    """Class to test serialize is working properly
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
        self.serializer = QuotationSerializer(instance=self.quotation_valid)

    def test_verify_serialized_fields(self):
        """Test to verify fields serializeds in serializer
        """
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['date', 'response_date']))

    def test_verify_correct_fields(self):
        """Test if value in fields still same after serialize
        """
        data = self.serializer.data
        self.assertEqual(data['date'], self.quotation_valid.date)
        self.assertEqual(data['response_date'], self.quotation_valid.response_date)
