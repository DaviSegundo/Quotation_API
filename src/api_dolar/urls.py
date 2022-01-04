from django.contrib import admin
from django.urls import path
from quotation.views import quotation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', quotation),
    path('quotation/', quotation),
]
