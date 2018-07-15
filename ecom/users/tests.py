from django.test import TestCase
from django.contrib.auth.models import User
from .views import *


class UserAuthTestCase(TestCase):
    def test_auth(self):
        user = User.objects.create_user('max', 'maxim@test.com', 'maxpass')
        user.first_name = "Maxim"
        user.last_name = "Smith"
        user.save()
        
        try: 
            user = User.objects.get(username="max", password="maxpass")
        except Exception as exc:
            pass

        if user is not None:
            print(user.username + ' authenticated successfully')
            # redirect to a success page.
        else:
            # return an 'invalid login' error message.
            print('User ' + user.username +  ' not Found')

