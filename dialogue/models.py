import datetime
from django.utils import timezone
from django.db import models

class Dialogue(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    child_id = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(
        default=timezone.now)

    def set_updated_date(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.question
