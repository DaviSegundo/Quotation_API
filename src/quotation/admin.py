from django.contrib import admin
from .models import Quotation

# Register your models here.

class ListQuotation(admin.ModelAdmin):
    list_display = ('date', 'response_date')

admin.site.register(Quotation, ListQuotation)
