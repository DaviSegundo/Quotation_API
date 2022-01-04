"""
Module to handler requests for quotations.
"""

from django.http import JsonResponse
from .models import Quotation


def quotation(request):
    """Return JSON response general.

    Keyword arguments:
    request -- parameters [ date, currency, days ]
    """
    args = request.GET.get('currency')
    print(args)
    quotations = Quotation()
    json_response = quotations.show_all()
    return JsonResponse(json_response)
