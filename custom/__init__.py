from django.contrib.auth.middleware import RemoteUserMiddleware
from CSH_PMS import settings
import os
__author__ = 'William'


class CustomHeaderMiddleware(RemoteUserMiddleware):
    header = 'HTTP_WEBAUTH_USER'
    def process_request(self, request):
        if settings.DEBUG and hasattr(os.environ,'REMOTE_USER'):
            request.META[self.header] = os.environ['REMOTE_USER']
        return RemoteUserMiddleware.process_request(self, request)