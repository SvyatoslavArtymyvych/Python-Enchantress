# Generated by Django 3.1.7 on 2021-04-26 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_auto_20210416_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]