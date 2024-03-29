# Generated by Django 5.0.1 on 2024-01-22 23:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Link",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("original_url", models.URLField(max_length=2000)),
                ("short_url", models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
