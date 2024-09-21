from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class AuthenticationEmail(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            get_user_object = user_model.objects.get(email=username)
            if get_user_object.check_password(password):
                return get_user_object
        except (user_model.DoesNotExist, user_model.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        get_user = get_user_model()
        try:
            return get_user.objects.get(pk=user_id)
        except get_user.DoesNotExists :
            return None