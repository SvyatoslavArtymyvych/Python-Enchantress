# Generated by Django 3.1.7 on 2021-04-08 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20210408_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='car_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car', verbose_name='photo'),
        ),
    ]
