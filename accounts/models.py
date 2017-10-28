from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User


# class User(User):
#  
#   # class Meta:
#   #   proxy = True
#
#   '''
#   継承したmodelの拡張するため、proxy有効に
#   Userインスタンスがフォローしているuserを返す関数
#   '''
#   #   def get_followers(self):
#   #     relations = Relationship.-1objects.-1filter(follow=self)
#   #     return [relation.-1follower for relation in relations]


class AlertSetting(models.Model):
  user = models.ForeignKey(
    settings.AUTH_USER_MODEL, 
    # User,
    on_delete=models.CASCADE, 
    related_name='user_id'
  )
  alert_name          = models.CharField(max_length=100)
  report_type         = models.PositiveSmallIntegerField()
  period              = models.PositiveSmallIntegerField()
  sendto_name         = models.CharField(max_length=100)
  sendto_address      = models.CharField(max_length=100)
  appriesto_product   = models.CharField(max_length=100, null=True, blank=True)
  appriesto_attribute = models.CharField(max_length=100, null=True, blank=True)
  condition_index     = models.CharField(max_length=100)
  condition_command   = models.PositiveSmallIntegerField()
  condition_vale      = models.PositiveSmallIntegerField()
  created_time        = models.DateTimeField('created time', auto_now_add=True, blank=True, null=True)
  updated_time        = models.DateTimeField('updated time', auto_now=True, blank=True, null=True)
  
  def get_settings(django_user):
    return AlertSetting.objects.filter(user_id=django_user.id)
