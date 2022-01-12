"""Configuration of Admin page -- quotations
"""

from django.contrib import admin
from .models import Quotation

# Register your models here.

class ListQuotation(admin.ModelAdmin):
    """Configure display show
    """
    list_display = ('date', 'response_date')
    search_fields = ('date',)

admin.site.register(Quotation, ListQuotation)
