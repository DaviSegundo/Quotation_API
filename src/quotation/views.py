"""
Module to handler requests for quotations.
"""

from django.http import JsonResponse
from .models import Quotation


def last_quotation(request):
    """Return JSON response general.
    """
    quotations = Quotation()
    json_response = quotations.show_all()

    return JsonResponse(json_response)


def quotation_by_date(request):
    """Return JSON data from a date.

    Keyword arguments:
    request -- parameters [ date ]
    """
    args = request.GET
    date = args.get('date', None)
    currency = args.get('currency', None)
    quotations = Quotation()
    if date is None:
        return JsonResponse(quotations.show_all())
    else:
        response_by_date = quotations.get_by_date(date=date, currency=currency)
        return JsonResponse(response_by_date)

def last_days_quotations(request):
    """Return last days quotations of a currency.

    Keyword arguments:
    request -- parameters [ days, currency ]
    """
    args = request.GET
    days = int(args.get('days', None))
    currency = args.get('currency', None)

    quotations = Quotation()
    quotations_list = quotations.get_past_days(days=days, currency=currency)

    return JsonResponse(quotations_list)