from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from settings.models import Profile
from skhufeeds import account

# backend for Authenticating user with url that includes JWT
class UrlTokenBackend(ModelBackend):
    def authenticate(self, useruid, token):
        print("Authenticating user {} with token {}".format(useruid, token))
        user = User.objects.get(username = useruid)
        if account.verifyToken(useruid, token):
            return user
        else:
            return None
