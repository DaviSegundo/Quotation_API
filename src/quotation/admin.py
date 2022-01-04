from django.contrib import admin
from .models import Quotation

# Register your models here.

class ListQuotation(admin.ModelAdmin):
    list_display = ('date', 'url_base')

admin.site.register(Quotation)
