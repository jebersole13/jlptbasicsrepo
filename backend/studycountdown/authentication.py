from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError


class SessionTokenAuthentication(JWTAuthentication):
    """
    Custom authentication backend that reads the JWT from a
    session cookie, falling back to a signed header for API clients.
    """

    COOKIE_NAME = 'session_token'
    HEADER_PREFIX = 'Token'

    def authenticate(self, request):
        raw_token = self._get_cookie_token(request)

        if raw_token is None:
            raw_token = self._get_header_token(request)

        if raw_token is None:
            return None

        return self._validate(raw_token)

    def _get_cookie_token(self, request):
        return request.COOKIES.get(self.COOKIE_NAME)

    def _get_header_token(self, request):
        header = request.META.get('HTTP_X_AUTH_TOKEN')
        if not header:
            return None
        parts = header.split()
        if len(parts) != 2 or parts[0] != self.HEADER_PREFIX:
            return None
        return parts[1]

    def _validate(self, raw_token):
        try:
            validated = self.get_validated_token(raw_token)
            user = self.get_user(validated)
            return user, validated
        except (InvalidToken, TokenError):
            return None