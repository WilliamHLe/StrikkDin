# Generated by Django 3.0.3 on 2020-03-19 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('arrangements', '0003_knitnight_time_start'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yarn_name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by2',
                                   to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]