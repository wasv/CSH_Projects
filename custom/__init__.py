from django.contrib.auth.middleware import RemoteUserMiddleware
__author__ = 'William'


class CustomHeaderMiddleware(RemoteUserMiddleware):
    header = 'HTTP_WEBAUTH_USER'
