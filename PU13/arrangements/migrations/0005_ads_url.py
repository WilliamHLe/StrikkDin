# Generated by Django 3.0.3 on 2020-03-19 22:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('arrangements', '0004_ads'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
