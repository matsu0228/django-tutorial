from django.db import models
from django.contrib.auth.models import User

def build_user_obj(django_user):
  brandname = django_user.get_username()
  user_obj["username"] = django_user.get_username()
  return user_obj
