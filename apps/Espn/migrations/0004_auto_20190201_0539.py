# Generated by Django 2.1.5 on 2019-02-01 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Espn', '0003_auto_20190127_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='forget_password_access_token',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
