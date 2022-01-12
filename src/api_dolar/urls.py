"""Definition of routes paths
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from quotation import views
from quotation.views import QuotationsViewSet

router = routers.DefaultRouter()
router.register('quotations', QuotationsViewSet, basename='Quotations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/quotation/', views.last_quotation),
    path('api/quotation/date/', views.quotation_by_date),
    path('api/quotation/days/', views.last_days_quotations),
    path('db/quotation/', views.db_last_quotation),
    path('db/quotation/<str:date>/', views.db_quotation_by_date),
    path('db/quotation/days/<int:days>/<str:currency>/', views.db_last_days_quotations),
    path('pop_bank/<int:items>/', views.pop_bank),
    path('serial/', views.test_serialize),
    path('search/', views.new_test_json_search),
]
