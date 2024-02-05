# Generated by Django 5.0.1 on 2024-02-04 15:35

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Feed",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "public_id",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.UUID("afc19cb0-b49f-4724-b03a-6c8179ea8b7d"),
                        editable=False,
                        unique=True,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("url", models.URLField()),
                ("global_search_pattern", models.CharField(max_length=200)),
                ("search_pattern", models.CharField(max_length=200)),
                ("feed_title", models.CharField(max_length=50)),
                ("feed_link", models.CharField(max_length=200)),
                ("feed_description", models.CharField(max_length=200)),
                ("item_title_template", models.CharField(max_length=12)),
                ("item_link_template", models.CharField(max_length=12)),
                ("item_content_template", models.CharField(max_length=12)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]