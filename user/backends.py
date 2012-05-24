'''
 Created by Syno Tech.
 User: Syno-Frank
 Date: 4/25/12
 Time: 11:53 AM
'''
from django.contrib.auth.models import User, Permission
class OpenidBackend(object):

    def authenticate(self, username=None, password=None):
        try:
            if '@' in username:
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None