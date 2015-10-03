from django.contrib.auth.middleware import RemoteUserMiddleware
from CSH_PMS import settings
__author__ = 'William'


class CustomHeaderMiddleware(RemoteUserMiddleware):
    header = 'HTTP_WEBAUTH_USER'
    def process_request(self, request):
        if settings.DEBUG:
            request.META[self.header] = 'wasv'
        return RemoteUserMiddleware.process_request(self, request)