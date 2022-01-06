"""Custom Middleware to check for new quotation on every request
"""

from quotation.utils.last_quotation import last_quotation

class LastQuotationMiddleware:
    """Handle request to get new quotations
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        last_quotation()

        response = self.get_response(request)
        return response
