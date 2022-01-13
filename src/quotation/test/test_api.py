"""Module with tests of API routes
"""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from quotation.models import Quotation


class QuotationsTestCase(APITestCase):
    """ Class to test API routes of quotations methods
    """

    def setUp(self):
        self.list_url = reverse('Quotations-list')
        self.quotation_1 = Quotation.objects.create(
            date='2020-12-24',
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
                }
            }
        )

    def test_request_get_quotations(self):
        """Testing GET request is working
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_post_quotations(self):
        """Testing POST to new quotations
        """
        data = {
            "date": "2002-12-24",
            "response_date": {
                "currency": "dale"
            }
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertAlmostEqual(response.status_code, status.HTTP_201_CREATED)

    def test_request_delete_quotations(self):
        """Testing DELETE is not allowed for quotations
        """
        response = self.client.delete(self.list_url)
        self.assertAlmostEqual(response.status_code,
                               status.HTTP_405_METHOD_NOT_ALLOWED)
