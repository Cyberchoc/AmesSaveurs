# Generated by Django 4.1.7 on 2023-02-22 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("salade", "0002_salade_thumbnail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="salade",
            name="thumbnail",
            field=models.ImageField(
                blank=True, null=True, upload_to="salade/static/salade/images/salades"
            ),
        ),
    ]
