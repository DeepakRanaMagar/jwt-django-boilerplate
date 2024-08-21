# Generated by Django 5.0.7 on 2024-08-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accounts",
            name="address",
            field=models.CharField(max_length=50, null=True, verbose_name="Address"),
        ),
        migrations.AlterField(
            model_name="accounts",
            name="phone_no",
            field=models.IntegerField(
                null=True, unique=True, verbose_name="Phone Number"
            ),
        ),
    ]
