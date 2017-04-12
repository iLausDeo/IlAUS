import datetime
import jsonfield, json

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class MsgPhone(models.Model):
    user = models.OneToOneField(User, primary_key=True)

    mobile_phone = models.CharField(max_length=16, blank=True)    
    phone_country = models.CharField(max_length=100, blank=True, default="china")
    phone_country_code = models.CharField(max_length=100, blank=True, default="+86")

    created_at = models.DateTimeField(default=timezone.now, null=True)
    credit = models.DecimalField(max_digits=16, decimal_places=11, default=0)
    

    

    class Meta:
        db_table = 'user_info'
