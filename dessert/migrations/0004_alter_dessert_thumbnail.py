# Generated by Django 4.1.7 on 2023-02-23 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dessert", "0003_alter_dessert_thumbnail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dessert",
            name="thumbnail",
            field=models.ImageField(
                blank=True, null=True, upload_to="static/dessert/images"
            ),
        ),
    ]
