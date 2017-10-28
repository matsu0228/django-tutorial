from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import time, json
from .models import AlertSetting

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
@login_required
def alert_settings(request):
  user = request.user
  page_objs = {
    'key': 'val', 
    'user_id': user.id,
    'alert': AlertSetting.get_settings(user),
               }
  data = json.dumps(page_objs)
  return HttpResponse(data, content_type='application/json')
