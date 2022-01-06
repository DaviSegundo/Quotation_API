"""Custom Middleware to check for new quotation on every request
"""

from quotation.utils.last_quotation import last_quotation

class LastQuotationMiddleware:
    """Handle request to get new quotations
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        url = request.get_full_path()
        url_sep = url.split('/')
        if url_sep[1] != "db":
            print(url_sep)
            last_quotation()

        response = self.get_response(request)
        return response
