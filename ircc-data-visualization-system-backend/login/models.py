from datetime import datetime
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid;

class UserProfile(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=250, blank=False, default='')
    user_gender = models.CharField(max_length=250, blank=False, default='male')
    user_birthdate = models.DateTimeField(default=datetime.now, blank=True)
    user_address = models.CharField(max_length=250, blank=True, default='')
    user_phone = models.CharField(max_length=250, blank=True, default='')
    user_icon = models.CharField(max_length=250, blank=True, default='')
    user_postcode = models.CharField(max_length=250, blank=True, default='')

    REQUIRED_FIELDS = []

    def __str__(self):
        return self

    class Meta:
        managed = True
        db_table = 'userprofile'