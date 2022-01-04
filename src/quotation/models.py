import requests
from django.db import models
from .utils.functions import working_days

# Create your models here.


class Quotation(models.Model):
    """Quotation class to handle requests.

    Keyword arguments:
    date -- date from currency quotation
    currency -- type of cash
    days -- days past
    """
    date = models.CharField(primary_key=True, max_length=15)
    url_base = 'https://api.vatcomply.com/rates?base=USD'
    response = requests.get(url_base).json()

    def show_all(self) -> dict:
        """Return last quotation
        """
        return self.response

    def get_date(self, response: dict = None) -> str:
        """Return date from a response
        """
        if response is None:
            return self.response.get('date', None)
        else:
            return response.get('date', None)

    def get_quotation(self, currency: str) -> float:
        currency = currency.upper()
        rates = self.response.get('rates', None)
        return rates.get(f'{currency}', None)

    def get_by_date(self, date: str, currency: str = None) -> dict:
        url_with_date = self.url_base + f"&date={date}"
        response_by_date = requests.get(url_with_date).json()
        if currency is None:
            return response_by_date
        else:
            currency = currency.upper()
            rates = response_by_date.get('rates', None)
            curr = rates.get(f'{currency}', None)
            resp = {'date' : date, f'{currency}': curr}
            return resp

    def get_past_days(self, days: int, currency: str) -> dict:
        dates = working_days(days)
        currency_list = []

        for date in dates:
            curr = self.get_by_date(date, currency)
            currency_list.append(curr)

        response = {'quotations': currency_list}
        return response
