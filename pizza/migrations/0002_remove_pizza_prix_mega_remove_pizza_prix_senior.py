# Generated by Django 4.1.7 on 2023-02-22 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pizza", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pizza",
            name="prix_mega",
        ),
        migrations.RemoveField(
            model_name="pizza",
            name="prix_senior",
        ),
    ]
