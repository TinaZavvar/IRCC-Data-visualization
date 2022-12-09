from datetime import datetime
from django.db import models
import uuid;

class Subscription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField(max_length=250, blank=True, default="")
    expire_date = models.DateTimeField(default=datetime.now, blank=True)
    plan_id = models.CharField(max_length=250, blank=True, default="none")

    class Meta:
        managed = True
        db_table = 'subscription'