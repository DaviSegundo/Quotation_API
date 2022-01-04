"""Definition of routes paths
"""

from django.contrib import admin
from django.urls import path
from quotation.views import last_quotation, quotation_by_date, last_days_quotations

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', last_quotation),
    path('quotation/', last_quotation),
    path('quotation/date', quotation_by_date),
    path('quotation/days', last_days_quotations),
]
