from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import user_passes_test
from .models import build_user_obj
import time, json


def is_brand_member(user):
  global user_obj
  user_obj = build_user_obj(user)
  return True

# @user_passes_test(is_brand_member, login_url='/accounts/login/')
def alert_setting(request):
  page_objs = { 'key': 'val',  }
  data = json.dumps(page_objs)
  return HttpResponse(data, content_type='application/json')
