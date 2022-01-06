"""Model for Class Quotation
"""

import requests
from django.db import models
from .utils.functions import working_days

class Quotation(models.Model):
    """Quotation class to handle requests.
    """
    date = models.CharField(primary_key=True, max_length=15)
    url_base = 'https://api.vatcomply.com/rates?base=USD'
    response = requests.get(url_base).json()
    response_date = models.JSONField()

    def show_all(self) -> dict:
        """Return last quotation by request
        """
        return self.response

    def get_date(self, response: dict = None) -> str:
        """Return date from a response

        Keyword arguments:
        response -- json with data
        """
        if response is None:
            return self.response.get('date', None)

        return response.get('date', None)

    def get_quotation_currency(self, currency: str) -> dict:
        """Return currency spec of last quotation

        Keyword arguments:
        currency -- type of cash
        """
        currency = currency.upper()
        rates = self.response.get('rates', None)
        value = rates.get(f'{currency}', None)
        return {"currency" : f'{value}'}

    def get_by_date(self, date: str, currency: str = None) -> dict:
        """Return JSON response by date or currency spec

        Keyword arguments:
        date -- date of quotation
        currency -- type of cash
        """
        url_with_date = self.url_base + f"&date={date}"
        response_by_date = requests.get(url_with_date).json()
        if currency is None:
            return response_by_date

        currency = currency.upper()
        rates = response_by_date.get('rates', None)
        curr = rates.get(f'{currency}', None)
        resp = {'date' : date, 'currency': curr}
        return resp

    def get_past_days(self, days: int, currency: str) -> dict:
        """Return last quotations of workingdays

        Keyword arguments:
        days -- days past
        currency -- type of cash
        """
        dates = working_days(days)
        currency_list = []

        for date in dates:
            curr = self.get_by_date(date, currency)
            currency_list.append(curr)

        currency_list.reverse()

        response = {'quotations': currency_list, 'currency': f'{currency.upper()}'}
        return response
