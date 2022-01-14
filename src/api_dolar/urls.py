"""Definition of routes paths
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from quotation import views
from quotation.views import QuotationsViewSet

router = routers.DefaultRouter()
router.register('quotations', QuotationsViewSet, basename='Quotations')

schema_view = get_schema_view(
   openapi.Info(
      title="Quotation API",
      default_version='v1',
      description="API to get information about currencys",
      terms_of_service="#",
      contact=openapi.Contact(email="davisp2009@hotmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('control/', admin.site.urls),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/quotation/', views.last_quotation),
    path('api/quotation/date/', views.quotation_by_date),
    path('api/quotation/days/', views.last_days_quotations),
    path('db/quotation/', views.db_last_quotation),
    path('db/quotation/<str:date>/', views.db_quotation_by_date),
    path('db/quotation/days/<int:days>/<str:currency>/', views.db_last_days_quotations),
    path('pop_bank/<int:items>/', views.pop_bank),
    path('serial/', views.test_serialize),
    path('serial_class/', views.test_serialize_with_class),
    path('search/', views.new_test_json_search),
]
