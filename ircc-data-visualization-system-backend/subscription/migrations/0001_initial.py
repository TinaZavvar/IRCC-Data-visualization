# Generated by Django 4.1 on 2022-11-28 02:37

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Subscription",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("user_id", models.CharField(blank=True, default="", max_length=250)),
                (
                    "expire_date",
                    models.DateTimeField(blank=True, default=datetime.datetime.now),
                ),
                (
                    "plan_id",
                    models.CharField(blank=True, default="none", max_length=250),
                ),
            ],
            options={
                "db_table": "subscription",
                "managed": True,
            },
        ),
    ]
