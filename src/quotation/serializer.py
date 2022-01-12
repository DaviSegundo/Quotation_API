"""Module to serialize model of quotation to API
"""

from rest_framework import serializers
from quotation.models import Quotation

class QuotationSerializer(serializers.ModelSerializer):
    """Quotation serializer class
    """
    class Meta:
        """Quotation informations that will be serialized
        """
        model = Quotation
        fields = ['date', 'response_date']
