"""Script to load data quotation on database.
"""

import os
import django
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api_dolar.settings")
django.setup()

from quotation.models import Quotation
from quotation.utils.functions import working_days

if __name__ == '__main__':
    # q = Quotation()

    # q.date = '2021-12-31'
    # q.save()

    dates = working_days(50)

    for date in dates:
        q = Quotation()
        q.date = date
        q.response_date = requests.get(
            f'https://api.vatcomply.com/rates?base=USD&date={date}').json()
        q.save()
