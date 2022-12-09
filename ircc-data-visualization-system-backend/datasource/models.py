from django.db import models
import uuid;

class ImmigrationStatusData(models.Model):
    id = models.CharField(primary_key=True, max_length=250, default=uuid.uuid4, editable=False)
    year = models.CharField(max_length=250, blank=True, unique=False, default="")
    gender = models.CharField(max_length=250, blank=True, unique=False, default="male")
    age = models.CharField(max_length=250, blank=True, unique=False, default="0")
    category = models.CharField(max_length=250, blank=True, unique=False, default="Canadian Experience Class")
    source = models.CharField(max_length=250, blank=True, unique=False, default="India")
    address = models.CharField(max_length=250, blank=True, unique=False, default="ON")
    status = models.CharField(max_length=250, blank=True, unique=False, default="In Progress")

    class Meta:
        managed = True
        db_table = 'immigration_data'

class CategoryData(models.Model):
    id = models.CharField(primary_key=True, max_length=250, default=uuid.uuid4, editable=False)
    year = models.CharField(max_length=250, blank=True, unique=False, default="0")
    federal_skilled_worker = models.CharField(max_length=250, blank=False, default="0")
    quebec_skilled_worker = models.CharField(max_length=250, blank=False, default="0")
    provincial_nominee_program = models.CharField(max_length=250, blank=False, default="0")
    family_sponsorship = models.CharField(max_length=250, blank=False, default="0")
    business_immigrant = models.CharField(max_length=250, blank=False, default="0")
    canadian_experience_class = models.CharField(max_length=250, blank=False, default="0")
    total = models.CharField(max_length=250, blank=False, default="0")

    class Meta:
        managed = True
        db_table = 'category_data'

class CountryData(models.Model):
    id = models.CharField(primary_key=True, max_length=250, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250, blank=True, unique=False, default="")
    total = models.CharField(max_length=250, blank=True, unique=False, default="0")

    class Meta:
        managed = True
        db_table = 'country_data'

class DestinationData(models.Model):
    id = models.CharField(primary_key=True, max_length=250, default=uuid.uuid4, editable=False)
    province = models.CharField(max_length=250, blank=True, unique=False, default="")
    federal_skilled_worker = models.CharField(max_length=250, blank=True, unique=False, default="0")
    quebec_skilled_worker = models.CharField(max_length=250, blank=False, default="0")
    provincial_nominee_program = models.CharField(max_length=250, blank=False, default="0")
    family_sponsorship = models.CharField(max_length=250, blank=False, default="0")
    business_immigrant = models.CharField(max_length=250, blank=False, default="0")
    canadian_experience_class = models.CharField(max_length=250, blank=False, default="0")
    total = models.CharField(max_length=250, blank=False, default="0")

    class Meta:
        managed = True
        db_table = 'destination_data'