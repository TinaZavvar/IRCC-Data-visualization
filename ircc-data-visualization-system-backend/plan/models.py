from django.db import models
import uuid;

class Plan(models.Model):
    id = models.CharField(max_length=250, primary_key=True, default=uuid.uuid4, editable=False)
    plan_name = models.CharField(max_length=250, blank=True, unique=True, default="free")
    plan_price = models.CharField(max_length=250, blank=True, default="0")
    plan_description = models.CharField(max_length=250, blank=True, default="")
    plan_image = models.CharField(max_length=250, blank=True, default="")

    class Meta:
        managed = True
        db_table = 'plan'