from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
import time, json

def loginview(request):
  current_user = request.user
  if request.method == "POST":
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user:
      login(request, user)
      return redirect('../alert_settings')
  else:
    return render(request, 'accounts/login.html')


# @user_passes_test(is_brand_member, login_url='/accounts/login/')
def alert_settings(request):
  page_objs = { 'key': 'val',  }
  data = json.dumps(page_objs)
  return HttpResponse(data, content_type='application/json')
