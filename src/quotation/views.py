"""
Module to handler requests for quotations.
"""

from rest_framework import viewsets
from django.http import JsonResponse

from quotation.utils.functions import working_days
from .serializer import QuotationSerializer
from .models import Quotation

# Requests made by direct requesto to third-party API

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

# API requests using restframework

class QuotationsViewSet(viewsets.ModelViewSet):
    """Show quotations saved in database
    """
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer

# API requests using database

def db_last_quotation(request):
    """Request to get last quotation saved in database
    """
    db_quotation = Quotation.objects.last()
    response = {"date" : db_quotation.date,
                "response_date" : db_quotation.response_date}
    return JsonResponse(response)

def db_quotation_by_date(request, date):
    """Request to get quotation by date saved in database

    Keyword arguments:
    date -- date of quotation
    """
    quotation_date = Quotation.objects.filter(date=date).first()
    response = {"date" : quotation_date.date,
                "response_date" : quotation_date.response_date}
    return JsonResponse(response)

def db_last_days_quotations(request, days: int, currency: str):
    """Request to get last days quotations of database

    Keyword arguments:
    days -- last days
    currency -- type of cash
    """
    dates = working_days(days=days)
    currency = currency.upper()
    quotations = []
    for date in dates:
        info = Quotation.objects.filter(date=date).first()
        value = info.response_date.get('rates').get(currency)
        response = {"date" : info.date, "currency" : value}
        quotations.append(response)
    quotations.reverse()
    final_response = {"quotations" : quotations, "currency" : currency.upper()}

    return JsonResponse(final_response)
