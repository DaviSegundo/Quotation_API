"""Function to save a new quotation in database
"""

import os
import django
import requests
from quotation.utils.functions import working_days

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api_dolar.settings")
django.setup()

from ..models import Quotation

def last_quotation(days = 1):
    """Save a new quotation from a request in API
    """
    dates = working_days(days)

    for date in dates:
        quotation = Quotation()
        quotation.date = date
        quotation.response_date = requests.get(
            f'https://api.vatcomply.com/rates?base=USD&date={date}').json()
        quotation.save()
